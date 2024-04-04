import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Locators
USER_NAME = ("css selector", "input[data-test='username']")
PASSWORD = ("css selector", "input[data-test='password']")
LOGIN = ("css selector", "input[id='login-button']")

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.find_element(*USER_NAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN).click()
    driver.set_window_size(1440, 1080)
    yield driver
    print('\nquit browser...')
    driver.quit()
