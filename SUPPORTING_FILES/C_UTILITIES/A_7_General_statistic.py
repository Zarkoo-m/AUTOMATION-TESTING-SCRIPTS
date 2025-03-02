import re
import datetime
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger

def collect_statistics(log_file_path, console_logs):
  

    stats = {
        "ACTION_COMPLETED": 0,
        "ACTION_FAILED": 0,
        "VALIDATION_SUCCESSFUL": 0,
        "VALIDATION_FAILED": 0,
        "SCREENSHOT_SUCCESS": 0,
        "SCREENSHOT_FAIL": 0,
        "DATA_STORED": 0,
        "HTML_STORED": 0,
        "GRAPHQL_CONFIRMED": 0,
        "GRAPHQL_FAILED": 0,
        "CONSOLE_LOGS": 0,
        "INFO_LOGS": 0,
        "WARNING_LOGS": 0,
        "ERROR_LOGS": 0,
    }

    total_actions = 0
    total_validations = 0
    total_screenshots = 0
    total_data = 0
    total_graphql = 0
    total_console_logs = 0

    first_timestamp = None
    
    last_seconds = None

 
    if console_logs:
        total_console_logs = len(console_logs)
        stats["CONSOLE_LOGS"] = total_console_logs
        
   
        for log in console_logs:
            log_type = log.get("level", "INFO").upper()
            if log_type == "INFO":
                stats["INFO_LOGS"] += 1
            elif log_type == "WARNING":
                stats["WARNING_LOGS"] += 1
            elif log_type == "ERROR":
                stats["ERROR_LOGS"] += 1

 
    with open(log_file_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
           
            timestamp_match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
            if timestamp_match:
                current_timestamp = datetime.datetime.strptime(timestamp_match.group(1), "%Y-%m-%d %H:%M:%S")
                if first_timestamp is None:
                    first_timestamp = current_timestamp
                

           
            match = re.search(r"-\s+([\d.]+) sec\s+-", line)
            if match:
                last_seconds = match.group(1)

           
            if "[ACTION COMPLETED]" in line:
                stats["ACTION_COMPLETED"] += 1
                total_actions += 1
            elif "[ACTION - FAILED]" in line:
                stats["ACTION_FAILED"] += 1
                total_actions += 1
            elif "[VALIDATION - SUCCESSFUL]" in line:
                stats["VALIDATION_SUCCESSFUL"] += 1
                total_validations += 1
            elif "[VALIDATION - FAILED]" in line:
                stats["VALIDATION_FAILED"] += 1
                total_validations += 1
            elif "[SCREENSHOT - SUCCESS]" in line:
                stats["SCREENSHOT_SUCCESS"] += 1
                total_screenshots += 1
            elif "[SCREENSHOT - FAIL]" in line:
                stats["SCREENSHOT_FAIL"] += 1
                total_screenshots += 1
            elif "[DATA STORED]" in line:
                stats["DATA_STORED"] += 1
                total_data += 1
            elif "[HTML STORED]" in line:
                stats["HTML_STORED"] += 1
                total_data += 1
            elif "[CONFIRMED - GRAPHQL - COMPARED]" in line:
                stats["GRAPHQL_CONFIRMED"] += 1
                total_graphql += 1
            elif "[NOT - CONFIRMED - GRAPHQL - COMPARED]" in line:
                stats["GRAPHQL_FAILED"] += 1
                total_graphql += 1

 
    total_time = last_seconds if last_seconds else "N/A"


    print("\n-------------------- {GENERAL SECTION} --------------------")
    print(f"TOTAL EXECUTION TIME: {total_time} sec")  
    print(f"[ACTION COMPLETED] : SUCCESSFUL {stats['ACTION_COMPLETED']} of {total_actions}")
    print(f"[ACTION - FAILED] : FAILED {stats['ACTION_FAILED']} of {total_actions}")
    print("----------------------------------------------------------\n")
    print(f"[VALIDATION - SUCCESSFUL] : SUCCESSFUL {stats['VALIDATION_SUCCESSFUL']} of {total_validations}")
    print(f"[VALIDATION - FAILED] : FAILED {stats['VALIDATION_FAILED']} of {total_validations}")
    print("----------------------------------------------------------\n")
    print(f"[SCREENSHOT - SUCCESS] : SUCCESSFUL {stats['SCREENSHOT_SUCCESS']} of {total_screenshots}")
    print(f"[SCREENSHOT - FAIL] : FAILED {stats['SCREENSHOT_FAIL']} of {total_screenshots}")
    print("----------------------------------------------------------\n")
    print(f"[DATA STORED] : {stats['DATA_STORED']} records stored")
    print(f"[HTML STORED] : {stats['HTML_STORED']} elements stored")
    print("----------------------------------------------------------\n")
    print(f"[GRAPHQL CONFIRMED] : SUCCESSFUL {stats['GRAPHQL_CONFIRMED']} of {total_graphql}")
    print(f"[GRAPHQL FAILED] : FAILED {stats['GRAPHQL_FAILED']} of {total_graphql}")
    print("----------------------------------------------------------\n")
    print(f"[CONSOLE LOGS] : {stats['CONSOLE_LOGS']} logs found")
    print(f"[INFO LOGS] : {stats['INFO_LOGS']} logs found")
    print(f"[WARNING LOGS] : {stats['WARNING_LOGS']} logs found")
    print(f"[ERROR LOGS] : {stats['ERROR_LOGS']} logs found")
    print("----------------------------------------------------------\n")


