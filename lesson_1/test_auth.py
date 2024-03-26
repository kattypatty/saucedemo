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

    # On inventory page, click on "Add to cart" button.
    browser.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']").click()

    # On inventory page, click on "Add to cart" button.
    browser.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']").click()

    # On inventory page, click on the cart.
    browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

    # On cart page, click on the "remove" button.
    browser.find_element(By.XPATH, "//*[@class='btn_secondary cart_button']").click()

    # On cart page, click to choose the item and click on "remove" button from the item page
    browser.find_element(By.XPATH, "//*[@class='inventory_item_name']").click()
    browser.find_element(By.XPATH, "//*[@class='btn_secondary btn_inventory']").click()

def test_item_page():
    test_auth_positive()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html'
    browser.find_elements(By.XPATH, "//*[@id='item_4_img_link']/img")[0].click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4', browser.current_url
    
    browser.find_element(By.XPATH, "//*[@class='inventory_details_back_button']").click()
    
    browser.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4', browser.current_url
    time.sleep(100)

    # browser.quit()


test_shopping_cart()
test_item_page()