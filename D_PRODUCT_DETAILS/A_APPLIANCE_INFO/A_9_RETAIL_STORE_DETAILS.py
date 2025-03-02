from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class RetailStoreDetails:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def enter_retail_store_details(self, value):
        print(" ")
        print("[ENTER RETAIL STORE DETAILS]")
        print(" ")
        
# (A) ------------------------- LOCATE 'RETAIL STORE DETAILS' LABEL --------------------------------------------------------------
        try:
            retail_store_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Retail Store Details')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(retail_store_label_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (RETAIL STORE DETAILS LABEL) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - RETAIL STORE DETAILS LABEL)", e)
            return

# (B) ------------------------- LOCATE 'RETAIL STORE DETAILS' INPUT FIELD --------------------------------------------------------------
        try:
            retail_store_input_locator = (By.XPATH, "//div[label/div[contains(text(), 'Retail Store Details')]]//input[@type='text']")
            retail_store_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(retail_store_input_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (RETAIL STORE DETAILS INPUT FIELD) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - RETAIL STORE DETAILS INPUT FIELD)", e)
            return

# (C) ------------------------- INPUT VALUE INTO FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            retail_store_input.clear()
            retail_store_input.send_keys(value)
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (RETAIL STORE DETAILS INPUT FIELD) / VALUE ENTERED: '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("RetailStoreDetails", "retail_store", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("RetailStoreDetails", "retail_store", retail_store_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(ENTERING VALUE - RETAIL STORE DETAILS INPUT FIELD) - '{value}'", e)
            return


# (D) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            current_value = retail_store_input.get_attribute('value')
            
            if current_value == value:
                logger.info(f"[VALIDATION - SUCCESSFUL] ")
            else:
                logger.error(f"[VALIDATION - FAILED] | (RETAIL STORE DETAILS INPUT FIELD) - Expected '{value}', but got '{current_value}'.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(RETAIL STORE DETAILS INPUT FIELD)", e)
