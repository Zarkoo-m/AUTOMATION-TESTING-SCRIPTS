from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class ModelSelection:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def enter_model_selection(self, value):
        print(" ")
        print("[MODEL SELECTION]")
        print(" ")
        
# (A) ------------------------- LOCATE 'MODEL SELECTION' LABEL --------------------------------------------------------------
        try:
            model_selection_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Model selection')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(model_selection_label_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (MODEL SELECTION LABEL) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - MODEL SELECTION LABEL)", e)
            return

# (B) ------------------------- LOCATE 'MODEL SELECTION' INPUT FIELD --------------------------------------------------------------
        try:
            model_selection_input_locator = (By.XPATH, "//div[label/div[contains(text(), 'Model selection')]]//input[@type='text']")
            model_selection_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(model_selection_input_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (MODEL SELECTION INPUT FIELD) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - MODEL SELECTION INPUT FIELD)", e)
            return

# (C) ------------------------- INPUT VALUE INTO FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            model_selection_input.clear()
            model_selection_input.send_keys(value)
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (MODEL SELECTION INPUT FIELD) / VALUE ENTERED: '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("ModelSelection", "model_selection", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("ModelSelection", "model_selection", model_selection_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - MODEL SELECTION INPUT FIELD)", e)
            return

# (D) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            current_value = model_selection_input.get_attribute('value')
            
            if current_value == value:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | (MODEL SELECTION INPUT FIELD) - Expected '{value}', but got '{current_value}'.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(MODEL SELECTION INPUT FIELD)", e)
