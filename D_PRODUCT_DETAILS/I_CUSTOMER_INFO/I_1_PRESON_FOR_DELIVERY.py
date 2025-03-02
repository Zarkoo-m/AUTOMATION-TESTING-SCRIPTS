from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class PersonForDelivery:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_person_for_delivery(self, person_name):
        print(" ")
        print(f"[PERSON FOR DELIVERY]")
        print(" ")

# (A) ------------------------- LOCATE 'PERSON FOR DELIVERY' INPUT FIELD --------------------------------------------------------------
        try:
            input_field_locator = (
                By.XPATH, "//input[contains(@class, 'input_field')]"
            )

            input_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(input_field_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (PERSON FOR DELIVERY INPUT) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - PERSON FOR DELIVERY INPUT)", e)
            return

# (B) ------------------------- ENTER TEXT INTO INPUT FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            input_field.clear()
            input_field.send_keys(person_name)

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (PERSON FOR DELIVERY INPUT) / VALUE ENTERED: '{person_name}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("PersonForDelivery", "person_for_delivery", person_name)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("PersonForDelivery", "person_for_delivery", input_field)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - PERSON FOR DELIVERY INPUT)", e)
            return

# (C) ------------------------- CONFIRM 'DELIVERY INSTRUCTIONS' APPEARANCE --------------------------------------------------------------
        delivery_instructions_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Delivery instructions')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(delivery_instructions_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(PERSON FOR DELIVERY CONFIRMATION)", e)