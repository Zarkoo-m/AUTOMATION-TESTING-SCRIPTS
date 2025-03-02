from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer

#----------------------------------------------------------------------------------------------------------------
class SelectBrandModel:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_brand_model(self, brand_model_label):
        print(" ")
        print(f"[SELECT BRAND & MODEL]")
        print(" ")
        
# (A) ------------------------- LOCATE BRAND & MODEL BUTTON --------------------------------------------------------------
        try:
            radio_button_locator = (By.XPATH, f"//span[contains(text(), '{brand_model_label}')]")
            radio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(radio_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SELECT BRAND & MODEL BUTTON) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(LOCATING - SELECT BRAND & MODEL BUTTON) - '{brand_model_label}'", e)
            return

# (B) ------------------------- CLICK BRAND & MODEL BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            radio_button.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SELECT BRAND & MODEL BUTTON) / CLICKED.")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("SelectBrandModel", "brand_model", brand_model_label)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("SelectBrandModel", "brand_model", radio_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(CLICK - SELECT BRAND & MODEL BUTTON) - '{brand_model_label}'", e)
            return

# (C) ------------------------- CONFIRM 'QUANTITY SELECTION' TEXT APPEARANCE --------------------------------------------------------------
        quantity_selection_label_locator = (By.XPATH, "//span[contains(text(), 'Quantity selection')]")
        quantity_selection_field_locator = (By.XPATH, "//input[@value='Quantity selection']")

        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(quantity_selection_label_locator)
            )
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(quantity_selection_field_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL] | 'Quantity selection' text and field are visible.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception(f"(QUANTITY SELECTION VALIDATION)", e)


            

