from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class YearOfProduction:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def select_year_of_production(self, value):
        print(" ")
        print("[YEAR OF PRODUCTION]")
        print(" ")
        
# (A) ------------------------- LOCATE 'YEAR OF PRODUCTION' LABEL --------------------------------------------------------------
        try:
            year_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Year of Production')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(year_label_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (YEAR OF PRODUCTION LABEL) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - YEAR OF PRODUCTION LABEL)", e)
            return

# (B) ------------------------- LOCATE 'YEAR OF PRODUCTION' SELECT BUTTON --------------------------------------------------------------
        try:
            select_button_locator = (By.XPATH, "//div[label/div[contains(text(), 'Year of Production')]]//button[@class='select_button']")
            select_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(select_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (YEAR OF PRODUCTION SELECT BUTTON) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - YEAR OF PRODUCTION SELECT BUTTON)", e)
            return

# (C) ------------------------- CLICK SELECT BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            select_button.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (YEAR OF PRODUCTION SELECT BUTTON) / CLICKED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(CLICKING - YEAR OF PRODUCTION SELECT BUTTON)", e)
            return

# (D) ------------------------- LOCATE AND CLICK YEAR OPTION --------------------------------------------------------------
        try:
            option_locator = (By.XPATH, f"//div[@class='select_menu_item' and text()='{value}']")
            option_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )
            
            #-----------ACTION-----------
            option_element.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (YEAR OF PRODUCTION OPTION) '{value}' SELECTED")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("YearOfProduction", "year_of_production", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("YearOfProduction", "year_of_production", option_element)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(SELECTING - YEAR OF PRODUCTION OPTION) - '{value}'", e)
            return

# (E) ------------------------- CONFIRM SELECTED VALUE --------------------------------------------------------------
        try:
            selected_value_locator = (By.XPATH, "//div[label/div[contains(text(), 'Year of Production')]]//span[@class='select_button_value']")
            selected_value_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(selected_value_locator)
            )
            
            selected_value = selected_value_element.text.strip()
            
            if selected_value == value:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | (YEAR OF PRODUCTION SELECT) - Expected '{value}', but got '{selected_value}'.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(YEAR OF PRODUCTION SELECT)", e)
