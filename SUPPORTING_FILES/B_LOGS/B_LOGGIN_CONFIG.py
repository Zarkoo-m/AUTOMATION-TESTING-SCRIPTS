import logging
import os
import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  
#----------------------------------------------------

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) 
#----------------------------------------------------

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "app.log")
file_handler = logging.FileHandler(desktop_path)
file_handler.setLevel(logging.DEBUG)
#----------------------------------------------------

def custom_time_format(record, datefmt=None):
    
    log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(record.created)) 
    elapsed_time = f"{record.relativeCreated / 1000:.1f} sec"
    return f"{log_time}    -    {elapsed_time}"

formatter = logging.Formatter('%(asctime)s    -    %(levelname)s    -    %(message)s')
formatter.converter = time.gmtime  
formatter.formatTime = custom_time_format  

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
#----------------------------------------------------

logger.addHandler(console_handler)
logger.addHandler(file_handler)
