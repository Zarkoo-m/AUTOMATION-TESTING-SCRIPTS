from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class AppliancePriceDetails:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    
    #----------------------------------------------------
    def enter_appliance_price_details(self, value):
        print(" ")
        print("[APPLIANCE PRICE DETAILS]")
        print(" ")
        
# (A) ------------------------- LOCATE 'APPLIANCE PRICE DETAILS' LABEL --------------------------------------------------------------
        try:
            appliance_price_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Appliance Price Details')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(appliance_price_label_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (APPLIANCE PRICE DETAILS LABEL) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - APPLIANCE PRICE DETAILS LABEL)", e)
            return

# (B) ------------------------- LOCATE 'APPLIANCE PRICE DETAILS' INPUT FIELD --------------------------------------------------------------
        try:
            appliance_price_input_container_locator = (By.XPATH, "//div[label/div[contains(text(), 'Appliance Price Details')]]/div[@class='input']")
            input_container = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(appliance_price_input_container_locator)
            )
            
            appliance_price_input_locator = (By.XPATH, ".//input[@class='input_input input_number']")
            appliance_price_input = input_container.find_element(*appliance_price_input_locator)
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (APPLIANCE PRICE DETAILS INPUT FIELD) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - APPLIANCE PRICE DETAILS INPUT FIELD)", e)
            return

# (C) ------------------------- INPUT VALUE INTO FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            appliance_price_input.click()
            appliance_price_input.clear()
            appliance_price_input.send_keys(value)
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (APPLIANCE PRICE DETAILS INPUT FIELD) / VALUE ENTERED: '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("AppliancePriceDetails", "appliance_price", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("AppliancePriceDetails", "appliance_price", appliance_price_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception(f"(ENTERING VALUE - APPLIANCE PRICE DETAILS) - '{value}'", e)
            return


# (D) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            current_value = appliance_price_input.get_attribute('value')
            
            if current_value.replace(',', '').replace(' ', '') == value.replace(',', '').replace(' ', ''):
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | (APPLIANCE PRICE DETAILS INPUT FIELD) - Expected '{value}', but got '{current_value}'.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(APPLIANCE PRICE DETAILS INPUT FIELD)", e)

