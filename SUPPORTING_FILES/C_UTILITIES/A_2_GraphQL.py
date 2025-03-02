import os
import json
import csv
import datetime
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from collections import OrderedDict

class GraphQLResponseChecker:
    def __init__(self, driver):
        self.driver = driver

    def fetch_second_last_graphql_request(self):
        try:
            print("\n[GRAPHQL RESPONSE CHECKER]\n")

            # --------- COLLECT ALL GRAPHQL ---------
            graphql_requests = [
                request for request in self.driver.requests
                if "graphql" in request.url and request.method == "POST"
            ]

            if len(graphql_requests) < 2:
                logger.error("[GRAPHQL - FAILED] | Less than 2 GraphQL requests detected!")
                print("(FAILED) | Less than 2 GraphQL requests detected!")
                return None

            #---------LAST GRAPHQL---------
            second_last_request = graphql_requests[-1]  

            # ------------------------- LAST GRAPHQL PAYLOAD -------------------------
            try:
                raw_payload = second_last_request.body.decode('utf-8')
                ordered_payload = json.loads(raw_payload, object_pairs_hook=OrderedDict)
                
                print("\n(SUCCESS) | GRAPHQL LAST - PAYLOAD:\n")

                # ------------------------- REMOVE ORDERS & SAVE -------------------------
                graphql_without_orders = self.remove_orders(ordered_payload)

                self.save_graphql_without_orders_to_csv(graphql_without_orders)

                # ------------------------- ORDERS EXTRACTION -------------------------
                orders_data = ordered_payload.get("variables", {}).get("ticket", {}).get("orders", None)

                if orders_data:
                    try:
                        orders_json = json.loads(orders_data, object_pairs_hook=OrderedDict)
                        self.save_orders_to_csv(orders_json)
                    except json.JSONDecodeError as e:
                        print(f"(FAILED) | Could not parse 'orders' as JSON. Error: {e}")
                else:
                    print("(FAILED) | 'orders' field not found in payload.")

            except json.JSONDecodeError as e:
                print(f"(FAILED) | Could not parse raw payload as JSON. Error: {e}")

        except Exception as e:
            logger.critical(f"(FAILED) > Error while fetching second last GraphQL request: {e}")
            print(f"(FAILED) > Error while fetching second last GraphQL request: {e}")
    
    #-----------------------------------------------------------------------------------------------------
    
    def remove_orders(self, graphql_json):
        try:
            # RETURN DICT
            if isinstance(graphql_json, str):
                graphql_json = json.loads(graphql_json, object_pairs_hook=OrderedDict)  
                
            graphql_without_orders = json.loads(json.dumps(graphql_json))  
            
            if "variables" in graphql_without_orders and "ticket" in graphql_without_orders["variables"]:
                if "orders" in graphql_without_orders["variables"]["ticket"]:
                    del graphql_without_orders["variables"]["ticket"]["orders"]
            return graphql_without_orders
        #-------------------------------------------------------------------
        except Exception as e:
            print(f"(FAILED) | Error while removing orders: {e}")
            return graphql_json
    #-----------------------------------------------------------------------------------------------------
    
    def save_orders_to_csv(self, orders_json):
        try:
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            filename = os.path.join(desktop_path, f"orders.csv")
            
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Key", "Value"])

                def write_dict_to_csv(d, parent_key=""):
                    if isinstance(d, dict):
                        for key, value in d.items():
                            full_key = f"{parent_key}.{key}" if parent_key else key
                            if isinstance(value, dict):
                                write_dict_to_csv(value, full_key)
                            elif isinstance(value, list):
                                for i, item in enumerate(value):
                                    write_dict_to_csv(item, f"{full_key}[{i}]")
                            else:
                                writer.writerow([full_key, value])
                    else:
                        writer.writerow(["orders", d])

                write_dict_to_csv(orders_json)

            print(f"(SUCCESS) | ORDERS data saved to CSV: {filename}")
        except Exception as e:
            print(f"(FAILED) | Could not save ORDERS data to CSV. Error: {e}")
            
    #-----------------------------------------------------------------------------------------------------
    
    def save_graphql_without_orders_to_csv(self, graphql_json):
        try:
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(desktop_path, f"graphql_without_orders_{timestamp}.csv")
            
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Key", "Value"])

                def write_dict_to_csv(d, parent_key=""):
                    if isinstance(d, dict):
                        for key, value in d.items():
                            full_key = f"{parent_key}.{key}" if parent_key else key
                            if isinstance(value, dict):
                                write_dict_to_csv(value, full_key)
                            elif isinstance(value, list):
                                for i, item in enumerate(value):
                                    write_dict_to_csv(item, f"{full_key}[{i}]")
                            else:
                                writer.writerow([full_key, value])

                write_dict_to_csv(graphql_json)

            print(f"(SUCCESS) | GraphQL payload without ORDERS saved to CSV: {filename}")
        except Exception as e:
            print(f"(FAILED) | Could not save GraphQL payload without ORDERS to CSV. Error: {e}")
