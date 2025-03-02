from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class InstallmentPlansAvailable:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_installment_plan(self, plan_option):
        print(" ")
        print(f"[INSTALLMENT PLANS AVAILABLE]")
        print(" ")

# (A) ------------------------- LOCATE INSTALLMENT PLAN BUTTON --------------------------------------------------------------
        try:
            installment_plan_locator = (By.XPATH, f"//span[@class='selection_button' and normalize-space(text())='{plan_option}']")
            installment_plan_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(installment_plan_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (INSTALLMENT PLAN OPTION) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - INSTALLMENT PLAN OPTION)", e)
            return

# (B) ------------------------- CLICK INSTALLMENT PLAN BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            installment_plan_button.click()

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (INSTALLMENT PLAN OPTION) / CLICKED '{plan_option}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("InstallmentPlansAvailable", "installment_plan", plan_option)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("InstallmentPlansAvailable", "installment_plan", installment_plan_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(CLICKING - INSTALLMENT PLAN OPTION)", e)
            return

# (C) ------------------------- CONFIRM 'CHOOSE INSTALLMENT PLAN' TEXT APPEARANCE --------------------------------------------------------------
        installment_plan_confirmation_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Choose installment plan')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(installment_plan_confirmation_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(INSTALLMENT PLAN CONFIRMATION)", e)

