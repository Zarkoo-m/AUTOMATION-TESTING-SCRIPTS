from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger

class StatusCode:
    
    def __init__(self, driver):
        self.driver = driver
    #-------------------------------------------
    def check_status_code(self):
        
        try:
            last_request = None
            for request in self.driver.requests:
                if "graphql" in request.url:  
                    last_request = request

            
            if last_request is None:
                logger.error("[STATUS - FAILED] | No GraphQL request detected after actions!")
            else:
                
                status_code = last_request.response.status_code

                
                if status_code == 200:
                    logger.info(f"[STATUS - SUCCESS] | Status Code: {status_code} (200 OK)")
                else:
                    logger.error(f"[STATUS - FAILED] | Unexpected Status Code: {status_code}")
        #-------------------------------------------------------------------------------------------------------
        except Exception as e:
            logger.critical(f"[STATUS - ERROR] | Unexpected error while fetching GraphQL response: {e}")
