import os
import time
import inspect
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger

class ScreenshotCapturer:
    def __init__(self, driver):
        self.driver = driver

        #-------------------------------------------
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.screenshot_directory = os.path.join(desktop_path, "AutomatioScreenshots")
        #-------------------------------------------
        try:
            
            os.makedirs(self.screenshot_directory, exist_ok=True)
            
        except Exception as e:
            logger.error(f"[ERROR CREATING DIRECTORY] | {e}")
    #-------------------------------------------
    def capture_screenshot(self):
        try:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            stack = inspect.stack()[1]

           
            class_name = stack.frame.f_locals.get("self", None).__class__.__name__ if "self" in stack.frame.f_locals else "NoClass"
            function_name = stack.function  

        
            filename = f"{class_name}_{function_name}_{timestamp}.png"
            screenshot_path = os.path.join(self.screenshot_directory, filename)

  
            self.driver.save_screenshot(screenshot_path)

            logger.info(f"[SCREENSHOT - SUCCESS]")
            
        #-------------------------------------------
        except Exception as e:
            logger.error(f"[SCREENSHOT - FAILED] | Error capturing screenshot: {e}")
           
