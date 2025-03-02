from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class StartNewPurchaseButton:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------------------
    def click_start_new_purchase(self):
        print(" ")
        print("[START NEW PURCHASE BUTTON]")
        print(" ")

# (A) ------------------------- LOCATE 'START NEW PURCHASE' BUTTON --------------------------------------------------------------
        try:
            start_new_purchase_button_locator = (By.XPATH, "//button[contains(text(), \"New purchase\")]")
            start_new_purchase_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(start_new_purchase_button_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (START NEW PURCHASE BUTTON) / LOCATED")

        #--------------------- EXCEPTION HANDLING---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - START NEW PURCHASE BUTTON)", e)
            return

       
# (B) ------------------------- CLICK 'START NEW PURCHASE' BUTTON --------------------------------------------------------------
        try:
            
            #-----------ACTION-----------
            start_new_purchase_button.click()
           
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (START NEW PURCHASE BUTTON) / CLICKED")
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING---------------------    
        except Exception as e:
            handle_action_exception("(START NEW PURCHASE BUTTON - CLICK)", e)
            return
        
       
        #------------------------- CONFIRMATION - ELEMENT 'WHAT TYPE OF APPLIANCE ARE YOU BUYING?' --------------------------------------------------------------
        try:
            appliance_type_label_locator = (By.XPATH, "//div[contains(text(), 'What type of appliance are you buying?')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(appliance_type_label_locator)
            )
            logger.info(f"[VALIDATION - SUCCESSFUL]")
            
        #--------------------- EXCEPTION HANDLING---------------------      
        except Exception as e:
            handle_validation_exception("(START NEW PURCHASE BUTTON)", e)
            return
