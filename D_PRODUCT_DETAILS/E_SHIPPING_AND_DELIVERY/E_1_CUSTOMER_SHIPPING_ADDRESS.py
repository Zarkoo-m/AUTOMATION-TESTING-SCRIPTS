from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class CustomerShippingAddress:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_customer_shipping_address(self, address_text):
        print(" ")
        print(f"[CUSTOMER SHIPPING ADDRESS] ")
        print(" ")

# (A) ------------------------- LOCATE 'CUSTOMER SHIPPING ADDRESS' INPUT FIELD --------------------------------------------------------------
        try:
            input_field_locator = (
                By.XPATH, "//input[contains(@class, 'input_field')]"
            )
            input_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(input_field_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CUSTOMER SHIPPING ADDRESS INPUT FIELD) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - CUSTOMER SHIPPING ADDRESS INPUT FIELD)", e)
            return

# (B) ------------------------- ENTER VALUE INTO INPUT FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            input_field.clear()
            input_field.send_keys(address_text)

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CUSTOMER SHIPPING ADDRESS INPUT FIELD) / VALUE ENTERED: '{address_text}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("CustomerShippingAddress", "customer_shipping_address", address_text)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("CustomerShippingAddress", "customer_shipping_address", input_field)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - CUSTOMER SHIPPING ADDRESS INPUT FIELD)", e)
            return

# (C) ------------------------- CONFIRM 'DELIVERY DATE AND TIME' TEXT APPEARANCE --------------------------------------------------------------
        delivery_date_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Delivery date and time')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(delivery_date_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(CUSTOMER SHIPPING ADDRESS CONFIRMATION)", e)

            
