from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Get selenium driver
def get_driver(driver, headless=True):
    options = Options()
    options.headless = True
    options.add_argument('log-level=3')
    caps = DesiredCapabilities.CHROME

    driver = webdriver.Chrome(
        executable_path = driver,
        options = options,
        desired_capabilities = caps
    )
    return driver
