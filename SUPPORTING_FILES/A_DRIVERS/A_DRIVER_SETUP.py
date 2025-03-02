from selenium import webdriver  
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from seleniumwire import webdriver as wire_webdriver  
import logging
#-------------------------------------------------------------------------
logging.getLogger('seleniumwire').setLevel(logging.ERROR)
#-------------------------------------------------------------------------
def setup_driver(browser_name="chrome", use_selenium_wire=False):
    if browser_name.lower() == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument('--disable-http2')
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})  

        driver = wire_webdriver.Chrome(service=service, options=options) if use_selenium_wire else webdriver.Chrome(service=service, options=options)
#-------------------------------------------------------------------------
    elif browser_name.lower() == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.set_preference("network.stricttransportsecurity.preloadlist", False)  
        options.set_preference("security.insecure_field_warning.contextual.enabled", False)
        options.set_preference("dom.security.https_only_mode", False)
        options.set_preference("webdriver.log.driver", "ALL")  

        driver = wire_webdriver.Firefox(service=service, options=options) if use_selenium_wire else webdriver.Firefox(service=service, options=options)
#-------------------------------------------------------------------------
    elif browser_name.lower() == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = EdgeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument('--disable-http2')
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})  

        driver = wire_webdriver.Edge(service=service, options=options) if use_selenium_wire else webdriver.Edge(service=service, options=options)

    else:
        raise ValueError("Unsupported browser: Use 'chrome', 'firefox', or 'edge'")
#-------------------------------------------------------------------------
    return driver
