from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.D_REUSABLE.D_2_NEXT_STEP_IN_ORDER_PROCESS import NextButtonRegular
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class SecurePaymentMethods:
    def __init__(self, driver):
        self.driver = driver
        self.Next_btn_regular = NextButtonRegular(driver)
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_payment_method(self, label_text):
        print(" ")
        print(f"[SECURE PAYMENT METHOD SELECTION]")
        print(" ")

# (A) ------------------------- LOCATE PAYMENT METHOD RADIO BUTTON BASED ON TEXT --------------------------------------------------------------
        try:
            payment_method_locator = (By.XPATH, f"//span[@class='selection_button' and normalize-space(text())='{label_text}']/ancestor::div[contains(@class, 'select_item_option')]")
            payment_method_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(payment_method_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SECURE PAYMENT METHOD) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - SECURE PAYMENT METHOD)", e)
            return

# (B) ------------------------- CLICK PAYMENT METHOD RADIO BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            payment_method_button.click()

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SECURE PAYMENT METHOD) / CLICKED '{label_text}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("SecurePaymentMethods", "payment_method", label_text)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("SecurePaymentMethods", "payment_method", payment_method_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(CLICKING - SECURE PAYMENT METHOD)", e)
            return

# (C) ------------------------- CONFIRM 'Next' BUTTON APPEARANCE --------------------------------------------------------------
        next_button_locator = (By.XPATH, "//button[contains(@class, 'next_btn') and contains(text(), 'Next')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(next_button_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(SECURE PAYMENT METHOD CONFIRMATION)", e)
        
# (D) ------------------------- NEXT BUTTON --------------------------------------------------------------
        self.Next_btn_regular.click_next_btn_regular()
