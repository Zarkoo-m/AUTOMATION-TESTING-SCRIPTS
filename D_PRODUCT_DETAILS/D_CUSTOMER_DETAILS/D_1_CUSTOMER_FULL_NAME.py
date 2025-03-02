from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class CustomerFullName:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_customer_name(self, customer_name):
        print(" ")
        print(f"[CUSTOMER FULL NAME] ")
        print(" ")

# (A) ------------------------- LOCATE 'CUSTOMER FULL NAME' INPUT FIELD --------------------------------------------------------------
        try:
            customer_name_locator = (
                By.XPATH, f"//span[@class='input_field' and text()='{customer_name}']"
            )
            customer_name_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(customer_name_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CUSTOMER FULL NAME) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - CUSTOMER FULL NAME)", e)
            return

# (B) ------------------------- INPUT CUSTOMER FULL NAME --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            customer_name_input.clear()  
            customer_name_input.send_keys(customer_name)  

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CUSTOMER FULL NAME) / ENTERED '{customer_name}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("CustomerFullName", "customer_name", customer_name)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("CustomerFullName", "customer_name", customer_name_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(ENTERING - CUSTOMER FULL NAME)", e)
            return

# (C) ------------------------- CONFIRM 'PLEASE ENTER CUSTOMER CONTACT DETAILS' TEXT APPEARANCE --------------------------------------------------------------
        contact_details_locator = (
            By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Please enter customer contact details')]"
        )
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(contact_details_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(CUSTOMER FULL NAME CONFIRMATION)", e)
