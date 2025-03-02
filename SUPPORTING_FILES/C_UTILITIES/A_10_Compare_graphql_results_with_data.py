import os
import csv
import json
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger

#---------------------------------------------------------
class GraphQLComparer:
    def __init__(self):
        #---------------------------------------------------------
        self.desktop_path = os.path.expanduser("~/Desktop")
        self.orders_file = os.path.join(self.desktop_path, "orders.csv")
        self.stored_data_file = os.path.join(self.desktop_path, "DATA STORED FROM SCRIPT", "Stored Data from script.csv")

        #---------------------------------------------------------
        self.comparison_keys = {
            "value_1": "response.order.data_1",
            "value_2": "response.order.data_2",
            "value_3": "response.order.data_3",
            "value_4": "response.order.data_4"
        }

    #---------------------------------------------------------
    def load_csv_to_dict(self, file_path, key_column=0, value_column=1):
        data_dict = {}
        if os.path.isfile(file_path):
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)  # Preskoči header
                for row in reader:
                    if len(row) >= 2:
                        key, value = row[key_column].strip(), row[value_column].strip()
                        data_dict[key] = value
        return data_dict

    #---------------------------------------------------------
    def extract_graphql_value_from_orders(self, graphql_key):
        try:
            if os.path.isfile(self.orders_file):
                with open(self.orders_file, mode="r", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    next(reader, None)  
                    for row in reader:
                        if len(row) >= 2 and graphql_key in row[0]:
                            return row[1]  
            return None
        except Exception as e:
            logger.error(f"(FAILED) | Could not extract {graphql_key} from ORDERS CSV: {e}")
            return None

    #---------------------------------------------------------
    def compare_graphql_values(self):
        stored_data = self.load_csv_to_dict(self.stored_data_file)

        for key, graphql_key in self.comparison_keys.items():
            script_value = stored_data.get(key, "N/A")
            graphql_value = self.extract_graphql_value_from_orders(graphql_key)

            if script_value == graphql_value:
                logger.info(f"[CONFIRMED - GRAPHQL - COMPARED] - {key} : {graphql_value}")
            else:
                logger.warning(f"[NOT - CONFIRMED - GRAPHQL - COMPARED] - {key} : {graphql_value}")
                logger.warning(f"NOTE: In data stored is {script_value} and in GraphQL is {graphql_value}")
