from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class AddNewAppliance:
    def __init__(self, driver):
        self.driver = driver
        
        self.screenshot_capturer = ScreenshotCapturer(driver)
    
    
    #----------------------------------------------------------------
    def add_new_appliance(self):
        print(" ")
        print("[ADD NEW APPLIANCE]")
        print(" ")

# (A) ------------------------- LOCATE 'ADD NEW' BUTTON --------------------------------------------------------------
        try:
            add_new_appliance_button_locator = (By.XPATH, "//button[contains(text(), 'Add new')]")
            add_new_appliance_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(add_new_appliance_button_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (ADD NEW APPLIANCE) / LOCATED.")

        #---------------------EXCEPTION HANDLING--------------------- 
        except Exception as e:
            handle_action_exception("(ADD NEW APPLIANCE)", e) 
            return

       
# (B) ------------------------- CLICK 'ADD NEW' BUTTON --------------------------------------------------------------
        try:
            
            #-----------ACTION-----------
            add_new_appliance_button.click()

            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (ADD NEW APPLIANCE BUTTON) / CLICKED")
                       
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
            
        #---------------------EXCEPTION HANDLING---------------------    
        except Exception as e:
            handle_action_exception("(ADD NEW APPLIANCE - CLICK)", e)  
            return
        
        
        # ------------------------- CONFIRM URL CHANGE --------------------------------------------------------------
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/appliance/new")
            )
            logger.info(f"[VALIDATION - SUCCESSFUL]")
            
        #---------------------EXCEPTION HANDLING---------------------      
        except Exception as e:
            handle_validation_exception("(ADD NEW APPLIANCE)", e)

