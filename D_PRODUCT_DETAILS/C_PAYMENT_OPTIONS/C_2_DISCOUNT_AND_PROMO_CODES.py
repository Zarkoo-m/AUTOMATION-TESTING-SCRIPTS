from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class DiscountAndPromoCodes:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_discount_or_promo_code(self, promo_code_option):
        print(" ")
        print(f"[DISCOUNT AND PROMO CODES]")
        print(" ")

# (A) ------------------------- LOCATE DISCOUNT OR PROMO CODE OPTION BUTTON --------------------------------------------------------------
        try:
            promo_code_option_locator = (By.XPATH, f"//span[@class='selection_button' and normalize-space(text())='{promo_code_option}']/ancestor::div[contains(@class, 'select_item_option')]")
            promo_code_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(promo_code_option_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (DISCOUNT AND PROMO CODE OPTION) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - DISCOUNT AND PROMO CODE OPTION)", e)
            return

# (B) ------------------------- CLICK DISCOUNT OR PROMO CODE OPTION BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            promo_code_button.click()

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (DISCOUNT AND PROMO CODE OPTION) / CLICKED '{promo_code_option}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("DiscountAndPromoCodes", "discount_promo", promo_code_option)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("DiscountAndPromoCodes", "discount_promo", promo_code_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(CLICKING - DISCOUNT AND PROMO CODE OPTION)", e)
            return

# (C) ------------------------- CONFIRM 'Would you like to apply a discount or promo code?' TEXT APPEARANCE --------------------------------------------------------------
        promo_code_confirmation_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Would you like to apply a discount or promo code?')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(promo_code_confirmation_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(DISCOUNT AND PROMO CODE CONFIRMATION)", e)

