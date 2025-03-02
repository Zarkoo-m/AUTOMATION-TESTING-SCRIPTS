from selenium.common.exceptions import TimeoutException, NoSuchElementException
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
from SUPPORTING_FILES.C_UTILITIES.A_5_Values_collector import stored_html 
# ---------------------------- EXCEPTION HANDLER FOR ACTIONS ----------------------------
def handle_action_exception(context, e):
    error_message = ""

    if isinstance(e, TimeoutException):
        error_message = f"[ACTION - FAILED] | ({context}) - Timeout: Not detected within timeframe!"
        
    elif isinstance(e, NoSuchElementException):
        error_message = f"[ACTION - FAILED] | ({context}) - Not found: {e}"
    else:
        error_message = f"[ACTION - FAILED] | ({context}) - Error: {e}"

    
    html_key = f"{context}.html"
    if html_key in stored_html:
        error_message += f"\n[SAVED HTML] | {context} | {stored_html[html_key]}"
    else:
        error_message += f"\n[SAVED HTML] | {context} | No HTML stored."

    logger.critical(error_message)

# ---------------------------- EXCEPTION HANDLER FOR VALIDATIONS ----------------------------
def handle_validation_exception(context, e):
    if isinstance(e, TimeoutException):
        logger.error(f"[VALIDATION - FAILED] | ({context}) - Timeout: Not detected within timeframe!")
    elif isinstance(e, NoSuchElementException):
        logger.error(f"[VALIDATION - FAILED] | ({context}) - Not found: {e}")
    else:
        logger.critical(f"[VALIDATION - FAILED] | ({context}) - Error: {e}")
