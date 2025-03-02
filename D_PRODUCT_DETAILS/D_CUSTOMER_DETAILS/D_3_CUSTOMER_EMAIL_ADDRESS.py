from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class CustomerEmailAddress:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_customer_email_address(self, email_value):
        print(" ")
        print(f"[CUSTOMER EMAIL ADDRESS] ")
        print(" ")

# (A) ------------------------- LOCATE 'CUSTOMER EMAIL ADDRESS' INPUT FIELD --------------------------------------------------------------
        try:
            input_field_locator = (By.XPATH, "//input[@placeholder='e.g. example@email.com' and contains(@class, 'input_field')]")
            input_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(input_field_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CUSTOMER EMAIL ADDRESS INPUT) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - CUSTOMER EMAIL ADDRESS INPUT)", e)
            return

# (B) ------------------------- ENTER VALUE INTO INPUT FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            input_field.clear()
            input_field.send_keys(email_value)
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CUSTOMER EMAIL ADDRESS INPUT) / VALUE ENTERED: '{email_value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("CustomerEmailAddress", "customer_email_address", email_value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("CustomerEmailAddress", "customer_email_address", input_field)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - CUSTOMER EMAIL ADDRESS INPUT)", e)
            return

# (C) ------------------------- CONFIRM 'EMAIL SUCCESSFULLY ENTERED' TEXT APPEARANCE --------------------------------------------------------------
        success_message_locator = (By.XPATH, "//span[contains(text(), 'Email successfully entered')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(success_message_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL] | 'Email successfully entered' message detected")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(CUSTOMER EMAIL ADDRESS CONFIRMATION)", e)
            return

