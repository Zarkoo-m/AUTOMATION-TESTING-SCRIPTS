from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.D_REUSABLE.D_2_NEXT_STEP_IN_ORDER_PROCESS import NextButtonRegular
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer


#----------------------------------------------------------------------------------------------------------------
class QuantitySelection:
    def __init__(self, driver):
        self.driver = driver
        self.Next_btn_regular = NextButtonRegular(driver)
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def select_quantity(self, value):
        print(" ")
        print(f"[QUANTITY SELECTION]")
        print(" ")
        
# (A) ------------------------- LOCATE QUANTITY SELECTION VALUE --------------------------------------------------------------
        try:
            quantity_button_locator = (By.XPATH, f"//span[contains(text(), '{value}')]/ancestor::div[@role='button']")
            quantity_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(quantity_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (QUANTITY SELECTION BUTTON) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(LOCATING - QUANTITY SELECTION BUTTON) - '{value}'", e)
            return

# (B) ------------------------- CLICK QUANTITY BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            quantity_button.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (QUANTITY SELECTION BUTTON) / CLICKED")
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(CLICK - QUANTITY SELECTION BUTTON) - '{value}'", e)
            return

# (C) ------------------------- CONFIRM 'NEXT' BUTTON APPEARANCE --------------------------------------------------------------
        next_button_locator = (By.XPATH, "//button[contains(text(), 'Next')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(next_button_locator)
            )
            logger.info(f"[VALIDATION - SUCCESSFUL]")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception(f"(QUANTITY SELECTION) - '{value}'", e)
        
        
# (E) ------------------------- NEXT BUTTON --------------------------------------------------------------
        self.Next_btn_regular.click_next_btn_regular()