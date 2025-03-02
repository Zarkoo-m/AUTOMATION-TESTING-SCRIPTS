from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class Email:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_email(self, email):
        print(" ")
        print(f"[EMAIL] ")
        print(" ")

# (A) ------------------------- LOCATE 'EMAIL' INPUT FIELD --------------------------------------------------------------
        try:
            input_field_locator = (
                By.XPATH,
                "//input[@type='email_address' and contains(@class, 'input_field') and contains(@class, 'input_field_email_address')]"
            )

            input_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(input_field_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (EMAIL INPUT) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - EMAIL INPUT)", e)
            return

# (B) ------------------------- ENTER VALUE INTO INPUT FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            input_field.clear()
            input_field.send_keys(email)

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (EMAIL INPUT) / VALUE ENTERED: '{email}'")
            
                        #-----------VALUE-COLLECTOR-----------
            Value_Collector("Email", "email", email)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("Email", "email", input_field)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()


        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - EMAIL INPUT)", e)
            return

# (C) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            entered_value = input_field.get_attribute("value")
            if entered_value == email:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | EMAIL > Value mismatch! Expected: '{email}', Found: '{entered_value}'")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(EMAIL CONFIRMATION)", e)
        

