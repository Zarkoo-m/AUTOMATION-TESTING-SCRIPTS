from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class ManualEntryOfDetails:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def select_manual_entry_of_details(self):
        print(" ")
        print("[MANUAL ENTRY OF DETAILS]")
        print(" ")
        
# (A) ------------------------- LOCATE 'MANUAL ENTRY OF DETAILS' OPTION BUTTON --------------------------------------------------------------
        try:
            manual_entry_option_locator = (By.XPATH, "//span[contains(@class, 'selection_button') and contains(text(), 'Manual')]")
            manual_entry_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(manual_entry_option_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (MANUAL OPTION) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - MANUAL OPTION)", e)
            return

# (B) ------------------------- CLICK 'MANUAL ENTRY OF DETAILS' OPTION BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            manual_entry_option.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (MANUAL ENTRY OF DETAILS OPTION) / CLICKED")
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(CLICK - MANUAL ENTRY OF DETAILS OPTION)", e)
            return
        

# (C) ------------------------- CONFIRM 'PRODUCT BRAND' TEXT DETECTED --------------------------------------------------------------
        product_brand_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Product brand')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(product_brand_label_locator)
            )
            logger.info(f"[VALIDATION - SUCCESSFUL] ")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(MANUAL ENTRY OF DETAILS OPTION)", e)

