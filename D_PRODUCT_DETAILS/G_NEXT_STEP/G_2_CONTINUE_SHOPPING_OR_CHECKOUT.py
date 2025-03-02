from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class ContinueShoppingOrCheckout:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_continue_shopping_or_checkout(self, value):
        print(" ")
        print(f"[CONTINUE SHOPPING OR CHECKOUT] ")
        print(" ")

# (A) ------------------------- LOCATE 'CONTINUE SHOPPING OR CHECKOUT' RADIO BUTTON --------------------------------------------------------------
        try:
            radio_button_locator = (
                By.XPATH,
                f"(//div[@class='lh-sm']//div[@class='input_field' and contains(text(), 'Would you like to continue shopping or proceed to checkout?')]/ancestor::div[@class='lh-sm']/following-sibling::div[@class='selection_button']//span[normalize-space(text())='{value}']/ancestor::div[@role='button'])[1]"
            )
            radio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(radio_button_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CONTINUE SHOPPING OR CHECKOUT OPTION) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - CONTINUE SHOPPING OR CHECKOUT OPTION)", e)
            return

# (B) ------------------------- CLICK RADIO BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            radio_button.click()

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CONTINUE SHOPPING OR CHECKOUT OPTION) / CLICKED '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("ContinueShoppingOrCheckout", "continue_shopping_or_checkout", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("ContinueShoppingOrCheckout", "continue_shopping_or_checkout", radio_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

            
        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(CLICKING - CONTINUE SHOPPING OR CHECKOUT OPTION)", e)
            return

# (C) ------------------------- CONFIRM 'PAYMENT METHOD SELECTION' QUESTION APPEARANCE --------------------------------------------------------------
        payment_method_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Please select your preferred payment method')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(payment_method_label_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(CONTINUE SHOPPING OR CHECKOUT CONFIRMATION)", e)
