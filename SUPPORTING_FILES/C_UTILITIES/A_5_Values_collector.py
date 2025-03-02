import os
import csv
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
#-------------------------------------------
stored_values = {} 
stored_html = {}  
#-------------------------------------------
folder_path = os.path.expanduser("~/Desktop/DATA STORED FROM SCRIPT")
os.makedirs(folder_path, exist_ok=True)
csv_file_path = os.path.join(folder_path, "Stored Data from script.csv")
file_exists = os.path.isfile(csv_file_path)

#-------------------------------------------
def Value_Collector(class_name, field_name, value):
    key = f"{class_name}.{field_name}"  
    stored_values[key] = value
    logger.info(f"[DATA STORED] | {key}|' {value}'") 

   
    write_to_csv(field_name, value)

#-------------------------------------------
def HTML_Collector(class_name, field_name, element):
    try:
        key = f"{class_name}.{field_name}.html"
        html_content = element.get_attribute("outerHTML")  
        stored_html[key] = html_content
        
        attributes = {
            "CLASS": element.get_attribute("class"),
            "ID": element.get_attribute("id"),
            "LABEL": element.get_attribute("aria-label"),
            "SPAN": element.get_attribute("span"),
            "TEXT": element.text,
            "ROLE": element.get_attribute("role"),
            "TYPE": element.get_attribute("type")
        }
        
        attributes_info = " | ".join([f"{attr}: {value if value else 'None'}" for attr, value in attributes.items()])
        
        logger.info(f"[HTML STORED] |{key}| {attributes_info}")  
    
    except Exception as e:
        logger.error(f"[HTML STORE FAILED] | {class_name}.{field_name} - Error: {e}")

#-------------------------------------------
def write_to_csv(key, value):
   
    with open(csv_file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["key", "value"])  
        writer.writerow([key.lower(), value])
