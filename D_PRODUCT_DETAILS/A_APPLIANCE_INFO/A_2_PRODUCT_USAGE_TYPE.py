from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class ProductUsageType:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_product_usage_type(self, option_label):
        print(" ")
        print(f"[PRODUCT USAGE TYPE]")
        print(" ")
        
# (A) ------------------------- LOCATE PRODUCT USAGE TYPE BUTTON --------------------------------------------------------------
        try:
            usage_option_locator = (By.XPATH, f"//span[contains(@class, 'selection_button') and contains(text(), '{option_label}')]")
            usage_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(usage_option_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (PRODUCT USAGE TYPE OPTION) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(LOCATING - PRODUCT USAGE TYPE OPTION) - '{option_label}'", e)
            return
        

# (B) ------------------------- CLICK PRODUCT USAGE TYPE BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            usage_option.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (PRODUCT USAGE TYPE OPTION) / CLICKED")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("ProductUsageType", "product_usage_type", option_label)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("ProductUsageType", "product_usage_type", usage_option)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(CLICK - PRODUCT USAGE TYPE OPTION) - '{option_label}'", e)
            return
        

# (C) ------------------------- CONFIRM 'DO YOU WISH TO SELECT PRODUCT DETAILS AUTOMATICALLY OR MANUALLY?' TEXT DETECTED --------------------------------------------------------------
        enter_product_details_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Do you wish to select product details automatically or manually?')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(enter_product_details_label_locator)
            )
            logger.info(f"[VALIDATION - SUCCESSFUL] ")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception(f"(PRODUCT USAGE TYPE) - '{option_label}'", e)

