
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class ApplianceCategory:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def select_appliance_category(self, value):
        print(" ")
        print("[APPLIANCE CATEGORY]")
        print(" ")
        
# (A) ------------------------- LOCATE 'APPLIANCE CATEGORY' LABEL --------------------------------------------------------------
        try:
            appliance_category_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Appliance Category')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(appliance_category_label_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (APPLIANCE CATEGORY LABEL) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - APPLIANCE CATEGORY LABEL)", e)
            return

# (B) ------------------------- LOCATE 'APPLIANCE CATEGORY' SELECT BUTTON --------------------------------------------------------------
        try:
            select_button_locator = (By.XPATH, "//div[label/div[contains(text(), 'Appliance Category')]]//button[@class='select_button']")
            select_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(select_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (APPLIANCE CATEGORY SELECT BUTTON) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - APPLIANCE CATEGORY SELECT BUTTON)", e)
            return

# (C) ------------------------- CLICK SELECT BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            select_button.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (APPLIANCE CATEGORY SELECT BUTTON) / CLICKED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(CLICKING - APPLIANCE CATEGORY SELECT BUTTON)", e)
            return


# (D) ------------------------- LOCATE AND CLICK APPLIANCE CATEGORY OPTION --------------------------------------------------------------
        try:
            option_locator = (By.XPATH, f"//div[@class='select_item' and contains(text(), '{value}')]")
            option_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )
            
            #-----------ACTION-----------
            option_element.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (APPLIANCE CATEGORY OPTION) '{value}' SELECTED")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("ApplianceCategory", "appliance_category", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("ApplianceCategory", "appliance_category", select_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(SELECTING - APPLIANCE CATEGORY OPTION) - '{value}'", e)
            return

# (E) ------------------------- CONFIRM SELECTED VALUE --------------------------------------------------------------
        try:
            selected_value_locator = (By.XPATH, "//div[label/div[contains(text(), 'Appliance Category')]]//span[@class='select_value']")
            selected_value_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(selected_value_locator)
            )
            
            selected_value = selected_value_element.text.strip()
            
            if selected_value == value:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | (APPLIANCE CATEGORY SELECT) - Expected '{value}', but got '{selected_value}'.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(APPLIANCE CATEGORY SELECT)", e)


