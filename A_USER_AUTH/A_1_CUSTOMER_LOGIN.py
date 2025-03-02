from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.D_REUSABLE.D_1_CONTINUE_TO_CHECKOUT import NextBtnLoginPage
from SUPPORTING_FILES.C_UTILITIES.A_1_Status_Code import StatusCode
from SUPPORTING_FILES.C_UTILITIES.A_2_GraphQL import GraphQLResponseChecker
from SUPPORTING_FILES.C_UTILITIES.A_3_Query import QueryResponseChecker
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import Value_Collector, HTML_Collector 
from SUPPORTING_FILES.C_UTILITIES.A_9_Exception_handler import handle_action_exception
from SUPPORTING_FILES.C_UTILITIES.A_6_Screenshots import ScreenshotCapturer
#----------------------------------------------------------------------------------------------------------------
class EmailFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.next_button_helper = NextBtnLoginPage(driver)
        self.status_code = StatusCode(driver)
        self.graphql_checker = GraphQLResponseChecker(driver)
        self.query_checker = QueryResponseChecker(driver)
        self.screenshot_capturer = ScreenshotCapturer(driver)
        
        
    #----------------------------------------------------------------
    def enter_email_and_click_next(self, email):
        print(" ")
        print("[LOGIN FORM - EMAIL]")
        print(" ")

# (A) ------------------------- EMAIL FIELD --------------------------------------------------------------
# EMAIL
        try:
            email_locator = (By.CSS_SELECTOR, "input[type='email']")
            email_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(email_locator)
            )

            #-----------ACTION-----------
            email_field.clear()
            email_field.send_keys(email)

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (EMAIL) - ENTERED : '{email}'.")
            print(" ")
                    
            #-----------VALUE-COLLECTOR-----------
            Value_Collector("EmailFormPage", "email", email)
            
            #-----------VALUE-COLLECTOR-----------
            HTML_Collector("EmailFormPage", "email", email_field)
            
            #-----------SCREENSHOT-CAPTURER-----------
            self.screenshot_capturer.capture_screenshot()
            
            
            # -------------- CONFIRMATION --------------
            if email_field.get_attribute("value") == email:
                logger.info(f"[VALIDATION - SUCCESSFUL]")
                
            else:
                logger.error(f"[VALIDATION - FAILED] | (EMAIL VALUE) > Expected '{email}' > but found '{email_field.get_attribute('value')}'.")
                
            print(" ")
        #--------------------- EXCEPTION HANDLING  ---------------------
        except Exception as e:
            handle_action_exception("EMAIL INPUT FIELD", e) 
            return

        
# (B) ------------------------- NEXT BUTTON ----------------------------------------------------------------
        self.next_button_helper.click_next_button()
        
# (C) ------------------------- STATUS CODE ----------------------------------------------------------------
        self.status_code.check_status_code()
        

        






