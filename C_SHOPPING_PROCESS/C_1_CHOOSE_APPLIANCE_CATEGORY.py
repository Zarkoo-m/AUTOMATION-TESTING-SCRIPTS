from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.D_REUSABLE.D_2_NEXT_STEP_IN_ORDER_PROCESS import NextButtonRegular
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector 
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer

#----------------------------------------------------------------------------------------------------------------
class SelectProductCategory:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def select_product_category(self, option_label):
        print(" ")
        print(f"[SELECT PRODUCT CATEGORY]")
        print(" ")
        
# (A) ------------------------- LOCATE PRODUCT CATEGORY BUTTON --------------------------------------------------------------
        try:
            radio_button_locator = (By.XPATH, f"//span[contains(text(), '{option_label}')]")
            radio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(radio_button_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SELECT PRODUCT CATEGORY BUTTON) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(LOCATING - SELECT PRODUCT CATEGORY BUTTON) - '{option_label}'", e)
            return

# (B) ------------------------- CLICK PRODUCT CATEGORY BUTTON --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            radio_button.click()
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (SELECT PRODUCT CATEGORY BUTTON) / CLICKED.")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("SelectProductCategory", "product_category", option_label)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("SelectProductCategory", "product_category", radio_button)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(CLICK - SELECT PRODUCT CATEGORY BUTTON) - '{option_label}'", e)
            return

# (C) ------------------------- CONFIRM 'HOW MANY PRODUCTS WILL BE PURCHASED?' TEXT APPEARANCE --------------------------------------------------------------
        products_purchased_label_locator = (By.XPATH, "//div[contains(text(), 'How many products will be purchased?')]")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(products_purchased_label_locator)
            )
            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception(f"(SELECT PRODUCT CATEGORY) - '{option_label}'", e)
        

        
