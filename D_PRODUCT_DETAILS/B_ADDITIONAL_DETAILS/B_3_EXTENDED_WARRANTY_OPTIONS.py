from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.D_REUSABLE.D_2_NEXT_STEP_IN_ORDER_PROCESS import NextButtonRegular
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class ExtendedWarrantyOptions:
    def __init__(self, driver):
        self.driver = driver
        self.Next_btn_regular = NextButtonRegular(driver)
        self.screenshot_capturer = ScreenshotCapturer(driver)
    
    #----------------------------------------------------
    def select_extended_warranty_options(self, value):
        print(" ")
        print(f"[EXTENDED WARRANTY OPTIONS] ")
        print(" ")
        
# (A) ------------------------- LOCATE 'EXTENDED WARRANTY OPTIONS' BUTTON --------------------------------------------------------------
        try:
            selection_button_locator = (
                By.XPATH,
                f"(//div[@class='input_field' and contains(text(), 'Is the product eligible for an extended warranty?')]/ancestor::div[contains(@class, 'lh-sm')]/following-sibling::div[@class='selection_button']//span[normalize-space(text())='{value}']/ancestor::div[contains(@class, 'select_item_option')])[1]"
            )
            selection_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(selection_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (EXTENDED WARRANTY OPTIONS) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - EXTENDED WARRANTY OPTIONS SELECTION BUTTON)", e)
            return

# (B) ------------------------- CLICK EXTENDED WARRANTY OPTIONS BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            selection_button.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (EXTENDED WARRANTY OPTIONS) / CLICKED '{value}'")
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(CLICKING - EXTENDED WARRANTY OPTIONS SELECTION BUTTON)", e)
            return

# (C) ------------------------- CONFIRM 'NEXT' BUTTON APPEARANCE --------------------------------------------------------------
        next_button_locator = (By.XPATH, "//button[contains(@class, 'btn_default_enabled') and contains(text(), 'Next')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(next_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL] | 'Next' button detected after clicking '{value}'")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(EXTENDED WARRANTY OPTIONS CONFIRMATION)", e)
        
# (D) ------------------------- NEXT BUTTON --------------------------------------------------------------
        self.Next_btn_regular.click_next_btn_regular()
