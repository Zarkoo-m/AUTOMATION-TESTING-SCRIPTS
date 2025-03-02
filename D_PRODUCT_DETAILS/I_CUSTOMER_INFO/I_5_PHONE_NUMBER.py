from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class PhoneNumber:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_phone_number(self, phone_number):
        print(" ")
        print(f"[PHONE NUMBER] ")
        print(" ")

# (A) ------------------------- LOCATE 'PHONE NUMBER' INPUT FIELD --------------------------------------------------------------
        try:
            input_field_locator = (
                By.XPATH,
                "//input[@type='phone_number' and contains(@class, 'input_field') and contains(@class, 'input_field_phone')]"
            )

            input_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(input_field_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (PHONE NUMBER INPUT) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - PHONE NUMBER INPUT)", e)
            return

# (B) ------------------------- ENTER VALUE INTO INPUT FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            input_field.clear()
            input_field.send_keys(phone_number)

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (PHONE NUMBER INPUT) / VALUE ENTERED: '{phone_number}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("PhoneNumber", "phone_number", phone_number)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("PhoneNumber", "phone_number", input_field)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()


        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - PHONE NUMBER INPUT)", e)
            return

# (C) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            entered_value = input_field.get_attribute("value")
            if entered_value == phone_number:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | PHONE NUMBER > Value mismatch! Expected: '{phone_number}', Found: '{entered_value}'")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(PHONE NUMBER CONFIRMATION)", e)
