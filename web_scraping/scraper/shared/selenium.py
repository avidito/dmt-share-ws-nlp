from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    """
    Getting selenium driver.
    """
    # Set up chrome options (compatible to run on container)
    options = Options()
    options.add_argument("log-level=3")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    chrome_prefs = {}
    options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

    # Create driver
    driver = webdriver.Chrome(options = options)
    return driver
