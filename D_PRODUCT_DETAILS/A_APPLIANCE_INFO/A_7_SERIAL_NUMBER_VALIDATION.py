from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class SerialNumberValidation:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_serial_number(self, value):
        print(" ")
        print("[SERIAL NUMBER VALIDATION]")
        print(" ")
        
# (A) ------------------------- LOCATE 'SERIAL NUMBER VALIDATION' LABEL --------------------------------------------------------------
        try:
            serial_number_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Serial Number Validation')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(serial_number_label_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SERIAL NUMBER VALIDATION LABEL) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - SERIAL NUMBER VALIDATION LABEL)", e)
            return

# (B) ------------------------- LOCATE 'SERIAL NUMBER VALIDATION' INPUT FIELD --------------------------------------------------------------
        try:
            serial_number_input_locator = (By.XPATH, "//div[label/div[contains(text(), 'Serial Number Validation')]]//input[@type='text']")
            serial_number_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(serial_number_input_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SERIAL NUMBER VALIDATION INPUT FIELD) / LOCATED")
             
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - SERIAL NUMBER VALIDATION INPUT FIELD)", e)
            return

# (C) ------------------------- INPUT VALUE INTO FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            serial_number_input.clear()
            serial_number_input.send_keys(value)
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SERIAL NUMBER VALIDATION INPUT FIELD) / VALUE ENTERED: '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("SerialNumberValidation", "serial_number", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("SerialNumberValidation", "serial_number", serial_number_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
         #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(ENTERING VALUE - SERIAL NUMBER VALIDATION INPUT FIELD) - '{value}'", e)
            return

# (D) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            current_value = serial_number_input.get_attribute('value')
            
            if current_value == value:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | (SERIAL NUMBER VALIDATION INPUT FIELD) - Expected '{value}', but got '{current_value}'.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(SERIAL NUMBER VALIDATION INPUT FIELD)", e)
