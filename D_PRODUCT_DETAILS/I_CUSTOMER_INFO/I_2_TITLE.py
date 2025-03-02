from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class Title:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_title(self, title):
        print(" ")
        print(f"[CUSTOMER TITLE] ")
        print(" ")

# (A) ------------------------- LOCATE ' TITLE' BUTTON --------------------------------------------------------------
        try:
            radio_button_locator = (
                By.XPATH,
                f"//span[@class='input_field' and normalize-space(text())='{title}']/ancestor::div[contains(@class, 'select_item')]"
            )

            radio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(radio_button_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (TITLE) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(LOCATING - TITLE OPTION)", e)
            return

# (B) ------------------------- CLICK 'TITLE' RADIO BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            radio_button.click()

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (TITLE) / CLICKED '{title}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("Title", "title", title)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("Title", "title", radio_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()


        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_action_exception("(CLICKING - TITLE OPTION)", e)
            return

# (C) ------------------------- CONFIRM 'FIRST NAME' APPEARANCE --------------------------------------------------------------
        first_name_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'First name')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(first_name_label_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------    
        except Exception as e:
            handle_validation_exception("(TITLE CONFIRMATION)", e)
