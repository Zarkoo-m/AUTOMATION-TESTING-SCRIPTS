from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer

class Finish:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def click_finish(self):
        print(" ")
        print("[CLICKING FINISH BUTTON]")
        print(" ")

# (A) ------------------------- CONFIRM 'SEGMENT PREVIEW' APPEARANCE --------------------------------------------------------------
        finall_step_locator = (By.XPATH, "//div[contains(@class, 'finall_step')]")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(finall_step_locator)
            )
            print("[VALIDATION - SUCCESSFUL] | 'finall_step_locator' detected.")
        
        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(FIANLL STEP CONFIRMATION)", e)
        
# (B) ------------------------- LOCATE 'FINISH' BUTTON AND CLICK --------------------------------------------------------------
        try:
            finish_button_locator = (By.XPATH, "//button[contains(@class, 'fisnish_btn_sx') and contains(text(), 'Finish')]")
            finish_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(finish_button_locator)
            )

            #-----------ACTION-----------
            finish_button.click()
            
            print("[ACTION COMPLETED] | 'finish button' button clicked.")
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(CLICKING - FINISH BUTTON)", e)
            return
