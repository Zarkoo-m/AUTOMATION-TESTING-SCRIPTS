from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer


#----------------------------------------------------------------------------------------------------------------
class SelectApplianceType:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)


    #----------------------------------------------------
    def select_appliance_type(self, option_label):
        print(" ")
        print(f"[SELECT APPLIANCE OPTION: {option_label}]")
        print(" ")
        
# (A) ------------------------- LOCATE APPLIANCE OPTION BASED ON TEXT --------------------------------------------------------------
        try:
            appliance_option_locator = (By.XPATH, f"//div[@role='button' and contains(., '{option_label}')]")
            appliance_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(appliance_option_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (APPLIANCE OPTION) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(LOCATING - APPLIANCE OPTION) - '{option_label}'", e)
            return

# (B) ------------------------- CLICK APPLIANCE OPTION --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            appliance_option.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (APPLIANCE OPTION) / CLICKED")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("SelectApplianceType", "appliance_type", option_label)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("SelectApplianceType", "appliance_type", appliance_option)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(CLICK - APPLIANCE OPTION) - '{option_label}'", e)
            return
       

# (C) ------------------------- CONFIRM 'SELECTED APPLIANCE DETAILS' TEXT APPEARANCE --------------------------------------------------------------
        appliance_condition_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Selected appliance details')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(appliance_condition_label_locator)
            )
            logger.info(f"[VALIDATION - SUCCESSFUL]")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception(f"(APPLIANCE OPTION) - '{option_label}'", e)
            


        
