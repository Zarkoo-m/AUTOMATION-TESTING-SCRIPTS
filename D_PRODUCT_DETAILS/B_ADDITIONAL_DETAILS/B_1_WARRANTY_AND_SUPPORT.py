from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class WarrantyAndSupport:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def select_warranty_and_support(self, value):
        print(" ")
        print(f"[WARRANTY AND SUPPORT] ")
        print(" ")
        
# (A) ------------------------- LOCATE 'WARRANTY AND SUPPORT' SELECTION BUTTON --------------------------------------------------------------
        try:
            selection_button_locator = (
                By.XPATH,
                f"(//div[@class='input_field' and contains(text(), 'Does the product include a warranty or support?')]/ancestor::div[contains(@class, 'px-1')]/following-sibling::div[@class='selection_button']//span[normalize-space(text())='{value}']/ancestor::div[contains(@class, 'selection_button_item')])[1]"
            )
            selection_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(selection_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (WARRANTY AND SUPPORT) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - WARRANTY AND SUPPORT SELECTION BUTTON)", e)
            return

# (B) ------------------------- CLICK SELECTION BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            selection_button.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (WARRANTY AND SUPPORT) / CLICKED '{value}'")
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(CLICKING - WARRANTY AND SUPPORT SELECTION BUTTON)", e)
            return

# (C) ------------------------- CONFIRM 'DOES THE CUSTOMER WANT AN EXTENDED WARRANTY?' TEXT APPEARANCE --------------------------------------------------------------
        extended_warranty_question_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Does the customer want an extended warranty?')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(extended_warranty_question_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL] |")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(WARRANTY AND SUPPORT CONFIRMATION)", e)



