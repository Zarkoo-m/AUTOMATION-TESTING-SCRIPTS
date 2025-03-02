from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class EnergyRating:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def enter_energy_rating(self, value):
        print(" ")
        print("[ENERGY RATING]")
        print(" ")
        
# (A) ------------------------- LOCATE 'ENERGY RATING' LABEL --------------------------------------------------------------
        try:
            energy_rating_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Energy Rating')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(energy_rating_label_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (ENERGY RATING LABEL) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - ENERGY RATING LABEL)", e)
            return

# (B) ------------------------- LOCATE 'ENERGY RATING' INPUT FIELD --------------------------------------------------------------
        try:
            energy_rating_input_locator = (By.XPATH, "//div[label/div[contains(text(), 'Energy Rating')]]//input[@type='text']")
            energy_rating_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(energy_rating_input_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (ENERGY RATING INPUT FIELD) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - ENERGY RATING INPUT FIELD)", e)
            return

# (C) ------------------------- INPUT VALUE INTO FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            energy_rating_input.clear()
            energy_rating_input.send_keys(value)
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (ENERGY RATING INPUT FIELD) / VALUE ENTERED: '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("EnergyRating", "energy_rating", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("EnergyRating", "energy_rating", energy_rating_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - ENERGY RATING INPUT FIELD)", e)
            return


# (D) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            current_value = energy_rating_input.get_attribute('value')
            
            if current_value == value:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | (ENERGY RATING INPUT FIELD) - Expected '{value}', but got '{current_value}'.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(ENERGY RATING INPUT FIELD)", e)

