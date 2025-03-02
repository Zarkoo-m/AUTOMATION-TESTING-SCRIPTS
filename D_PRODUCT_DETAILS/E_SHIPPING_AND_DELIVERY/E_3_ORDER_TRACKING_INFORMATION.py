from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class OrderTrackingInformation:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_order_tracking_information(self, tracking_info):
        print(" ")
        print(f"[ORDER TRACKING INFORMATION] ")
        print(" ")

# (A) ------------------------- LOCATE 'ORDER TRACKING INFORMATION' INPUT FIELD --------------------------------------------------------------
        try:
            tracking_input_locator = (
                By.XPATH, "//input[@type='text' and contains(@class, 'input_field')]"
            )
            tracking_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(tracking_input_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (ORDER TRACKING INFORMATION INPUT) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - ORDER TRACKING INFORMATION INPUT)", e)
            return

# (B) ------------------------- ENTER VALUE INTO INPUT FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            tracking_input.clear()
            tracking_input.send_keys(tracking_info)

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (ORDER TRACKING INFORMATION INPUT) / VALUE ENTERED: '{tracking_info}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("OrderTrackingInformation", "order_tracking_information", tracking_info)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("OrderTrackingInformation", "order_tracking_information", tracking_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - ORDER TRACKING INFORMATION INPUT)", e)
            return

# (C) ------------------------- CONFIRM 'ORDER CONFIRMATION AND TOTAL' TEXT APPEARANCE --------------------------------------------------------------
        order_confirmation_locator = (By.XPATH, "//span[contains(text(), 'Order confirmation and total')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(order_confirmation_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(ORDER TRACKING INFORMATION CONFIRMATION)", e)
        
