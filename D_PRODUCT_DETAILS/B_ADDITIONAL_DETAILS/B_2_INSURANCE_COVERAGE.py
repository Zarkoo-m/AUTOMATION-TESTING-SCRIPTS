from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class InsuranceCoverage:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)
    
    #----------------------------------------------------
    def select_insurance_coverage(self, value):
        print(" ")
        print(f"[INSURANCE COVERAGE]")
        print(" ")
        
# (A) ------------------------- LOCATE 'INSURANCE COVERAGE OPTION' SELECTION BUTTON --------------------------------------------------------------
        try:
            selection_button_locator = (
                By.XPATH,
                f"(//div[@class='input_field' and contains(text(), 'Does the product include insurance coverage?')]/ancestor::div[contains(@class, 'lh-sm')]/following-sibling::div[@class='selection_button']//span[normalize-space(text())='{value}']/ancestor::div[contains(@class, 'select_item_option')])[1]"
            )
            selection_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(selection_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (INSURANCE COVERAGE OPTION) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - INSURANCE COVERAGE OPTION SELECTION BUTTON)", e)
            return

# (B) ------------------------- CLICK SELECTION BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            selection_button.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (INSURANCE COVERAGE OPTION) / CLICKED '{value}'")
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(CLICKING - INSURANCE COVERAGE OPTION SELECTION BUTTON)", e)
            return

# (C) ------------------------- CONFIRM 'IS THE PRODUCT ELIGIBLE FOR AN EXTENDED WARRANTY?' TEXT APPEARANCE --------------------------------------------------------------
        extended_warranty_question_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Is the product eligible for an extended warranty?')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(extended_warranty_question_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL] ")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(INSURANCE COVERAGE OPTION CONFIRMATION)", e)
