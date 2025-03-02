from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.D_REUSABLE.D_2_NEXT_STEP_IN_ORDER_PROCESS import NextButtonRegular
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class WarehouseLocation:
    def __init__(self, driver):
        self.driver = driver
        self.Next_btn_regular = NextButtonRegular(driver)
        self.screenshot_capturer = ScreenshotCapturer(driver)
    
    #----------------------------------------------------
    def enter_warehouse_location(self, value):
        print(" ")
        print("[WAREHOUSE LOCATION]")
        print(" ")
        
# (A) ------------------------- LOCATE 'WAREHOUSE LOCATION' LABEL --------------------------------------------------------------
        try:
            warehouse_location_label_locator = (By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Warehouse Location')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(warehouse_location_label_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (WAREHOUSE LOCATION LABEL) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - WAREHOUSE LOCATION LABEL)", e)
            return

# (B) ------------------------- LOCATE 'WAREHOUSE LOCATION' INPUT FIELD --------------------------------------------------------------
        try:
            warehouse_location_input_locator = (By.XPATH, "//div[label/div[contains(text(), 'Warehouse Location')]]//input[@type='text']")
            warehouse_location_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(warehouse_location_input_locator)
            )
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (WAREHOUSE LOCATION INPUT FIELD) / LOCATED")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - WAREHOUSE LOCATION INPUT FIELD)", e)
            return

# (C) ------------------------- INPUT VALUE INTO FIELD --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            warehouse_location_input.clear()
            warehouse_location_input.send_keys(value)
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (WAREHOUSE LOCATION INPUT FIELD) / VALUE ENTERED: '{value}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("WarehouseLocation", "warehouse_location", value)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("WarehouseLocation", "warehouse_location", warehouse_location_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(ENTERING VALUE - WAREHOUSE LOCATION INPUT FIELD)", e)
            return

# (D) ------------------------- CONFIRM INPUT VALUE --------------------------------------------------------------
        try:
            current_value = warehouse_location_input.get_attribute('value')
            
            if current_value == value:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            else:
                logger.error(f"[VALIDATION - FAILED] | (WAREHOUSE LOCATION INPUT FIELD) - Expected '{value}', but got '{current_value}'.")
            
        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(WAREHOUSE LOCATION INPUT FIELD)", e)

        
# (E) ------------------------- NEXT BUTTON --------------------------------------------------------------
        self.Next_btn_regular.click_next_btn_regular()