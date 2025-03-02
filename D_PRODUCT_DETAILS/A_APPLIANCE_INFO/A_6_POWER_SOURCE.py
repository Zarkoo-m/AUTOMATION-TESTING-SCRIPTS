from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class PowerSource:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def enter_power_source(self, value):
        print(" ")
        print("[POWER SOURCE]")
        print(" ")
        
# (A) ------------------------- LOCATE 'POWER SOURCE' LABEL --------------------------------------------------------------
        try:
            power_source_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Power Source')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(power_source_label_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (POWER SOURCE LABEL) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - POWER SOURCE LABEL)", e)
            return

# (B) ------------------------- LOCATE 'POWER SOURCE' INPUT FIELD --------------------------------------------------------------
        try:
            power_source_input_locator = (By.XPATH, "//div[label/div[contains(text(), 'Power Source')]]//input[@type='text']")
            power_source_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(power_source_input_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (POWER SOURCE INPUT FIELD) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - POWER SOURCE INPUT FIELD)", e)
            return

# (C) ------------------------- INPUT VALUE INTO FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            power_source_input.clear()
            power_source_input.send_keys(value)
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (POWER SOURCE INPUT FIELD) / VALUE ENTERED: '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("PowerSource", "power_source", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("PowerSource", "power_source", power_source_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(ENTERING VALUE - POWER SOURCE INPUT FIELD) - '{value}'", e)
            return

# (D) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            current_value = power_source_input.get_attribute('value')
            
            if current_value == value:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | (POWER SOURCE INPUT FIELD) - Expected '{value}', but got '{current_value}'.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(POWER SOURCE INPUT FIELD)", e)

