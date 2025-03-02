from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class FirstName:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_first_name(self, first_name_value):
        print(" ")
        print(f"[FIRST NAME] ")
        print(" ")

# (A) ------------------------- LOCATE 'FIRST NAME' INPUT FIELD --------------------------------------------------------------
        try:
            input_field_locator = (
                By.XPATH,
                "//div[contains(@class, 'input_form') and contains(@class, 'lh-sm')]"
                "[.//div[@class='input_field' and contains(text(), 'Firstname')]]"
                "//input[@type='text' and contains(@class, 'input_field')]"
            )

            input_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(input_field_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (FIRST NAME INPUT) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - FIRST NAME INPUT)", e)
            return

# (B) ------------------------- ENTER VALUE INTO INPUT FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            input_field.clear()
            input_field.send_keys(first_name_value)

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (FIRST NAME INPUT) / VALUE ENTERED: '{first_name_value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("FirstName", "first_name", first_name_value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("FirstName", "first_name", input_field)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()


        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - FIRST NAME INPUT)", e)
            return

# (C) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            entered_value = input_field.get_attribute("value")
            if entered_value == first_name_value:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | FIRST NAME > Value mismatch! Expected: '{first_name_value}', Found: '{entered_value}'")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(FIRST NAME CONFIRMATION)", e)
