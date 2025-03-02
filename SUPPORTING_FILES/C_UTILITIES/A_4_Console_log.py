from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
import time

class ConsoleLogChecker:
    
    def __init__(self, driver):
        self.driver = driver

    #-------------------------------------------
    def fetch_console_logs(self):
      
        try:
            print("\n[CONSOLE LOG FETCHER]\n")
            time.sleep(2)  

            
            logs = self.driver.get_log("browser")
            if not logs:
                logger.warning("[CONSOLE - WARNING] | No console logs found!")
                print("[CONSOLE - WARNING] | No console logs found!")
                return None

            print("(SUCCESS) | ALL CONSOLE LOGS:")
            
          

            info_count, warning_count, error_count = 0, 0, 0

            for log in logs:
                log_type = log.get("level", "INFO").upper()  
                message = log.get("message", "").strip()  
                timestamp = log.get("timestamp", "")

                log_entry = f"{timestamp} | {log_type}: {message}"

                if log_type == "WARNING":
                    print(f"[WARNING] {message}")
                    logger.warning(log_entry)
                    warning_count += 1

                elif log_type == "ERROR":
                    print(f"[ERROR] {message}")
                    logger.error(log_entry)
                    error_count += 1

                else:
                    print(f"[INFO] {message}")
                    logger.info(log_entry)
                    info_count += 1

            print("-" * 50)

           
            print(f"INFO logs: {info_count}")
            print(f"WARNING logs: {warning_count}")
            print(f"ERROR logs: {error_count}")

            return logs  

        except Exception as e:
            logger.critical(f"[CONSOLE - ERROR] | Unexpected error while fetching console logs: {e}")
            print(f"[CONSOLE - ERROR] | Unexpected error while fetching console logs: {e}")

