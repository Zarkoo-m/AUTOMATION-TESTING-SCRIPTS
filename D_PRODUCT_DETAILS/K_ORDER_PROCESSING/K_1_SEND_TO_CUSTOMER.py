from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class SendToCustomer:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def send_to_customer(self):
        print(" ")
        print(f"[SEND TO CUSTOMER] ")
        print(" ")

# (A) ------------------------- LOCATE 'NO' RADIO BUTTON --------------------------------------------------------------
        try:
            send_locator = (
                By.XPATH,
                "//div[@type='button' and contains(@class, 'selection_button')]//span[text()='send']/.."
            )

            send_click = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(send_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SEND TO CUSTOMER) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - SEND TO CUSTOMER)", e)
            return

# (B) ------------------------- CLICK 'NO' RADIO BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            send_click.click()

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SEND TO CUSTOMER) / CLICKED")
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(CLICKING - SEND TO CUSTOMER)", e)
            return

# (C) ------------------------- CONFIRM 'FULL ORDER SENT' APPEARANCE --------------------------------------------------------------
        confirmation_locator = (By.XPATH, "//span[contains(text(), 'Full order sent to customer successfully')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(confirmation_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL] | 'Full order sent to customer successfully' detected.")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(SEND TO CUSTOMER CONFIRMATION)", e)
