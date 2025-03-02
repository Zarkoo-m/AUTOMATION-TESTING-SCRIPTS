from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class SendOrderConfirmationEmail:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_send_order_confirmation_email(self, value):
        print(" ")
        print(f"[SEND ORDER CONFIRMATION EMAIL] ")
        print(" ")

# (A) ------------------------- LOCATE 'SEND ORDER CONFIRMATION EMAIL' RADIO BUTTON --------------------------------------------------------------
        try:
            radio_button_locator = (
                By.XPATH,
                f"(//div[@class='lh-sm']//div[@class='input_field' and contains(text(), 'Would you like to send an order confirmation email?')]/ancestor::div[@class='lh-sm']/following-sibling::div[@class='selection_button']//span[normalize-space(text())='{value}']/ancestor::div[@role='button'])[1]"
            )
            radio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(radio_button_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SEND ORDER CONFIRMATION EMAIL OPTION) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - SEND ORDER CONFIRMATION EMAIL OPTION)", e)
            return

# (B) ------------------------- CLICK RADIO BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            radio_button.click()

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SEND ORDER CONFIRMATION EMAIL OPTION) / CLICKED '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("SendOrderConfirmationEmail", "send_order_confirmation_email", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("SendOrderConfirmationEmail", "send_order_confirmation_email", radio_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()


        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(CLICKING - SEND ORDER CONFIRMATION EMAIL OPTION)", e)
            return

# (C) ------------------------- CONFIRM 'ORDER CONFIRMED SUCCESSFULLY' MESSAGE APPEARANCE --------------------------------------------------------------
        order_confirmed_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Order confirmed successfully')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(order_confirmed_label_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(SEND ORDER CONFIRMATION EMAIL CONFIRMATION)", e)

