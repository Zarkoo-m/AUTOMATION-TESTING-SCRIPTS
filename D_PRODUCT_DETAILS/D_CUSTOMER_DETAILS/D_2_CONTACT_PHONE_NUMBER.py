from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception,handle_validation_exception
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class ContactPhoneNumber:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_capturer = ScreenshotCapturer(driver)

    #----------------------------------------------------
    def enter_contact_phone_number(self, phone_number):
        print(" ")
        print(f"[CONTACT PHONE NUMBER] ")
        print(" ")

# (A) ------------------------- LOCATE 'CONTACT PHONE NUMBER' INPUT FIELD --------------------------------------------------------------
        try:
            phone_number_locator = (
                By.XPATH, "//input[@class='selection_button' and @type='text']"
            )
            phone_number_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(phone_number_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CONTACT PHONE NUMBER) / LOCATED")

        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(LOCATING - CONTACT PHONE NUMBER)", e)
            return

# (B) ------------------------- INPUT PHONE NUMBER --------------------------------------------------------------
        try:
            #-----------ACTION-----------
            phone_number_input.clear()  
            phone_number_input.send_keys(phone_number)  
            
            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (CONTACT PHONE NUMBER) / ENTERED '{phone_number}'")
            
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("ContactPhoneNumber", "phone_number", phone_number)
            
            #-----------HTML-COLLECTOR-----------
            HTML_Collector("ContactPhoneNumber", "phone_number", phone_number_input)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()

        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_action_exception("(ENTERING - CONTACT PHONE NUMBER)", e)
            return

# (C) ------------------------- CONFIRM 'PLEASE ENTER CUSTOMER EMAIL ADDRESS' TEXT APPEARANCE --------------------------------------------------------------
        email_address_locator = (
            By.XPATH, "//div[contains(@class, 'input_field') and contains(text(), 'Please enter customer email address')]"
        )
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(email_address_locator)
            )

            #-----------ACTION-LOGGER-----------
            logger.info(f"[VALIDATION - SUCCESSFUL]")

        #--------------------- EXCEPTION HANDLING ---------------------
        except Exception as e:
            handle_validation_exception("(CONTACT PHONE NUMBER CONFIRMATION)", e)
