from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
import time
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InputValidation:
    def __init__(self, driver):
        self.driver = driver
    #-----------------------------------------------------
    def validate_input_field(self, field_locator):
       
        try:
            print("[INPUT VALIDATION]")
            print(" ")
            
            input_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(field_locator)
            )
            #-----------------------------------------------------
            input_field.clear()
            input_field.send_keys("12345")  
            time.sleep(1)
            entered_value = input_field.get_attribute("value")
            #-----------------------------------------------------
            if entered_value.isdigit():
                logger.info("[INPUT CHECK] | Field accepts numeric values. Testing alphabetic input...")
                input_field.clear()
                input_field.send_keys("ABCDE")  
                time.sleep(1)
                new_value = input_field.get_attribute("value")
                if new_value.isalpha():
                    logger.error("[VALIDATION FAILED] | Field incorrectly accepts alphabetic input!")
                else:
                    logger.info("[VALIDATION SUCCESS] | Field correctly rejects alphabetic input.")
            #-----------------------------------------------------        
            elif all(c in string.ascii_letters for c in entered_value):
                logger.info("[INPUT CHECK] | Field accepts alphabetic values. Testing numeric input...")
                input_field.clear()
                input_field.send_keys("12345") 
                time.sleep(1)
                new_value = input_field.get_attribute("value")
                if new_value.isdigit():
                    logger.error("[VALIDATION FAILED] | Field incorrectly accepts numeric input!")
                else:
                    logger.info("[VALIDATION SUCCESS] | Field correctly rejects numeric input.")
            else:
                logger.warning("[INPUT CHECK] | Field accepts mixed or unexpected input format.")
        #--------------------------------------------------------------------------------------------------
        except Exception as e:
            logger.error(f"[INPUT VALIDATION ERROR] | Error validating input field: {e}")
            print(f"[INPUT VALIDATION ERROR] | Error validating input field: {e}")