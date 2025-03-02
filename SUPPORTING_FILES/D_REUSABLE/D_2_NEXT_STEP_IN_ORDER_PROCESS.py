from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_1_Status_Code import StatusCode 
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception

#----------------------------------------------------------------------------------------------------------------
class NextButtonRegular:
    def __init__(self, driver):
        self.driver = driver
        self.status_code = StatusCode(driver) 
    
    #----------------------------------------------------
    def click_next_btn_regular(self):
        print(" ")
        print("[NEXT BUTTON ]")
        print(" ")
        
# (A) ------------------------- LOCATE 'NEXT' BUTTON --------------------------------------------------------------
        try:
            next_button_locator = (By.XPATH, "//button[contains(text(), 'Next')]")
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(next_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info("[ACTION COMPLETED] | LOCATED.")
        
        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - NEXT BUTTON )", e)
            return

# (B) ------------------------- CLICK 'NEXT' BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            next_button.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info("[ACTION COMPLETED] |  CLICKED.")
            
            #-----------STATUS CODE-----------
            self.status_code.check_status_code() 
           
        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("( CLICK - NEXT BUTTON )", e)
            return


