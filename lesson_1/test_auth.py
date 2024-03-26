from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()

def test_auth_positive():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'

def test_shopping_cart():
    test_auth_positive()
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

    time.sleep(10)

    # browser.quit()


test_shopping_cart()