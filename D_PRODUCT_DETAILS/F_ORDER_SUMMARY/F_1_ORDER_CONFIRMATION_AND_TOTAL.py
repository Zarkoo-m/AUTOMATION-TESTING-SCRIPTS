from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class OrderConfirmationAndTotal:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_order_confirmation_and_total(self, value):
        print(" ")
        print(f"[ORDER CONFIRMATION AND TOTAL] ")
        print(" ")

# (A) ------------------------- LOCATE RADIO BUTTON BASED ON QUESTION --------------------------------------------------------------
        try:
            radio_button_locator = (
                By.XPATH,
                f"(((//div[@class='lh-sm'])[1]/div[@class='lh-sm']/label/div[contains(text(), \"Do you want to confirm the total order?\")])/ancestor::div[@class='lh-sm']/following-sibling::div[@class='selection_button']//span[normalize-space(text())='{value}']/ancestor::div[contains(@class, 'select_item_option')])[1]"
            )

            radio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(radio_button_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (ORDER CONFIRMATION AND TOTAL OPTION) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - ORDER CONFIRMATION AND TOTAL OPTION)", e)
            return

# (B) ------------------------- CLICK RADIO BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            radio_button.click()

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (ORDER CONFIRMATION AND TOTAL OPTION) / CLICKED '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("OrderConfirmationAndTotal", "order_confirmation_and_total", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("OrderConfirmationAndTotal", "order_confirmation_and_total", radio_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()


        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(CLICKING - ORDER CONFIRMATION AND TOTAL OPTION)", e)
            return

# (C) ------------------------- CONFIRM 'send_order_confirmation_email' TEXT APPEARANCE --------------------------------------------------------------
        confirmation_locator = (By.XPATH, "//span[contains(text(), 'send_order_confirmation_email')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(confirmation_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(ORDER CONFIRMATION AND TOTAL CONFIRMATION)", e)

