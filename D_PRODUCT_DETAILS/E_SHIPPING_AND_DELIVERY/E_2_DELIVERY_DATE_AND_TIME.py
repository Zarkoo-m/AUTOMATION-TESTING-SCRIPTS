from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class DeliveryDateAndTime:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_delivery_date_and_time(self, delivery_text):
        print(" ")
        print(f"[DELIVERY DATE AND TIME] ")
        print(" ")

# (A) ------------------------- LOCATE 'DELIVERY DATE AND TIME' INPUT FIELD --------------------------------------------------------------
        try:
            input_field_locator = (
                By.XPATH, "//input[contains(@class, 'input_field')]"
            )
            input_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(input_field_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (DELIVERY DATE AND TIME INPUT FIELD) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - DELIVERY DATE AND TIME INPUT FIELD)", e)
            return

# (B) ------------------------- ENTER VALUE INTO INPUT FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            input_field.clear()
            input_field.send_keys(delivery_text)

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (DELIVERY DATE AND TIME INPUT FIELD) / VALUE ENTERED: '{delivery_text}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("DeliveryDateAndTime", "delivery_date_and_time", delivery_text)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("DeliveryDateAndTime", "delivery_date_and_time", input_field)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - DELIVERY DATE AND TIME INPUT FIELD)", e)
            return

# (C) ------------------------- CONFIRM 'ORDER TRACKING INFORMATION' TEXT APPEARANCE --------------------------------------------------------------
        order_tracking_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Order tracking information')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(order_tracking_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(DELIVERY DATE AND TIME CONFIRMATION)", e)
