from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_1_Status_Code import StatusCode
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class SelectOffer:
    def __init__(self, driver):
        self.driver = driver
        self.status_code = StatusCode(driver)
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def click_select(self):
        print(" ")
        print("[SELECT OFFER]")
        print(" ")

# (A) ------------------------- LOCATE 'SELECT' BUTTON --------------------------------------------------------------
        try:
            select_button_locator = (By.XPATH, "//button[contains(text(), 'Select') and contains(@class, 'btn_select_finall_offer')]")
            select_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(select_button_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SELECT BUTTON) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - SELECT BUTTON)", e)
            return

# (B) ------------------------- CLICK 'SELECT' BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            select_button.click()
            
            #------------- STATUS CODE------------
            self.status_code.check_status_code()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SELECT BUTTON) / CLICKED")
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(CLICKING - SELECT BUTTON)", e)
            return

# (C) ------------------------- CONFIRM 'OFFER SENT SUCCESSFULLY' TEXT APPEARANCE ------------------------------
        offer_sent_confirmation_locator = (By.XPATH, "//span[contains(text(), 'Offer sent successfully, check email for more information')]")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(offer_sent_confirmation_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL] | 'Offer sent successfully' message detected.")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(OFFER SENT CONFIRMATION)", e)

        
