# utils/browser_setup.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_browser():
    # Set up Chrome options (e.g., headless mode, if required)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    # Initialize Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    return driver
