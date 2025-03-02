from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger

class NextBtnLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_next_button(self):
        try:
            next_button_locator = (By.XPATH, "//button[contains(text(), 'Next')]")
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(next_button_locator)
            )

            #-----------ACTION-----------
            next_button.click()

            #-----------ACTION-LOGGER-----------
            logger.info(f"[ACTION COMPLETED] | (NEXT BUTTON) - CLICKED.")

            # -------------- CONFIRMATION --------------
            confirmation_locator = (By.XPATH, "//p[contains(text(), 'Enter the code you received on your phone.')]")

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(confirmation_locator)
                )
                logger.info(f"[VALIDATION - SUCCESSFUL]")
            except TimeoutException:
                logger.error(f"[VALIDATION - FAILED] | Next page did not detected !")

        #--------------------- EXCEPTION HANDLING FOR NEXT BUTTON ---------------------
        except TimeoutException:
            logger.error(f"[ACTION - FAILED] | (NEXT BUTTON) - Timeout: Not detected within timeframe!")
        except NoSuchElementException as e:
            logger.error(f"[ACTION - FAILED] | (NEXT BUTTON) - Not found : Next button not found: {e}")
        except Exception as e:
            logger.critical(f"[ACTION - FAILED] | (NEXT BUTTON) - Error : while clicking 'Next': {e}")
