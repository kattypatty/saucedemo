import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.set_window_size(1440, 1080)
    yield driver
    print('\nquit browser...')
    driver.quit()
