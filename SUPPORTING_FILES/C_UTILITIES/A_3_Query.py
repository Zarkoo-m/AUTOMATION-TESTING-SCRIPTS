
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
import json
from collections import OrderedDict

class QueryResponseChecker:
    
    def __init__(self, driver):
        self.driver = driver

    #-------------------------------------------
    def fetch_query_response(self):
        
        try:
            print("\n[QUERY RESPONSE & PAYLOAD FETCHER]\n")

            
            query_requests = [
                request for request in self.driver.requests
                if "/query" in request.url and request.method == "POST"
            ]

            if not query_requests:
                logger.error("[QUERY - FAILED] | No /query POST requests found.")
                print("[QUERY - FAILED] | No /query POST requests found.")
                return None

            last_request = query_requests[-1]  

            # (A) ------------------------- LAST QUERY PAYLOAD -------------------------
            try:
                raw_payload = last_request.body.decode('utf-8')
                ordered_payload = json.loads(raw_payload, object_pairs_hook=OrderedDict)  
                print(f"\n(SUCCESS) | QUERY LAST -  PAYLOAD:\n")
                print(self.format_dict(ordered_payload))

            except Exception as e:
                print(f"(FAILED) | Could not parse query payload as JSON. Error: {e}")

            # (B) ------------------------- LAST QUERY RESPONSE -------------------------
            try:
                if last_request.response and last_request.response.body:
                    raw_response = last_request.response.body.decode('utf-8')
                    ordered_response = json.loads(raw_response, object_pairs_hook=OrderedDict)  
                    print(f"\n(SUCCESS) | QUERY RAW RESPONSE:\n")
                    print(self.format_dict(ordered_response))

                    return ordered_response 

                else:
                    print(f"(FAILED) | No response body found for /query request!")

            except Exception as e:
                print(f"(FAILED) | Could not parse query response as JSON. Error: {e}")

        except Exception as e:
            logger.critical(f"(FAILED) > Error while fetching /query responses: {e}")
            print(f"(FAILED) > Error while fetching /query responses: {e}")

    #-------------------------------------------
    def format_dict(self, data):
       
        def format_recursive(d, level=0):
            output = ""
            for key, value in d.items():
                if isinstance(value, dict):
                    if level == 0:
                        output += f"\n{key.upper()}\n{'-' * 30}\n"
                    else:
                        output += f"\n{key.upper()}\n{'_' * 20}\n"
                    output += format_recursive(value, level + 1)
                elif isinstance(value, list):
                    output += f"\n{key.upper()}\n{'_' * 20}\n"
                    for item in value:
                        if isinstance(item, dict):
                            output += format_recursive(item, level + 1)
                        else:
                            output += f"{key}: {item}\n"
                else:
                    output += f"{key}: {value}\n"
            return output

        return format_recursive(data)
