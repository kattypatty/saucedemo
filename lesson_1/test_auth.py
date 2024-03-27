from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser=webdriver.Chrome()

def test_auth_positive():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'

# def test_shopping_cart():
#     test_auth_positive()

#     # On inventory page, click on "Add to cart" button.
#     browser.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']").click()

#     # On inventory page, click on "Add to cart" button.
#     browser.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']").click()

#     # On inventory page, click on the cart.
#     browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

#     # On cart page, click on the "remove" button.
#     browser.find_element(By.XPATH, "//*[@class='btn_secondary cart_button']").click()

#     # On cart page, click to choose the item and click on "remove" button from the item page
#     browser.find_element(By.XPATH, "//*[@class='inventory_item_name']").click()
#     browser.find_element(By.XPATH, "//*[@class='btn_secondary btn_inventory']").click()

# def test_item_page():
#     test_auth_positive()
#     assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html'

#     # On invenroty page, click on item image and page successfully transfers
#     browser.find_elements(By.XPATH, "//*[@id='item_4_img_link']/img")[0].click()
#     assert browser.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4', browser.current_url
    
#     # On image page, click on "back" button to come back to the inventory page
#     browser.find_element(By.XPATH, "//*[@class='inventory_details_back_button']").click()

#     #  On invenroty page, click on a product name and page successfully transfers 
#     browser.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").click()
#     assert browser.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4', browser.current_url
    

# def test_placing_order():
#     test_auth_positive()

#     # On inventory page, click on "Add to cart" button.
#     browser.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']").click()

#     # On inventory page, click on the cart.
#     browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

#     # On an item page, click on "checkout" button and page successfully transfers 
#     browser.find_element(By.XPATH, "//*[@class='btn_action checkout_button']").click()
#     assert browser.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html', browser.current_url
    
#     # Placing customer details in the checkout info
#     browser.find_element('xpath', "//*[@id='first-name']").send_keys('Vasya')
#     browser.find_element('xpath', "//*[@id='last-name']").send_keys('Petrov')
#     browser.find_element('xpath', "//*[@id='postal-code']").send_keys('98660')

#     time.sleep(5)
#     # On checkout information page, click on "continue" button and page successfully transfers
#     browser.find_element(By.XPATH, "//*[@class='btn_primary cart_button']").click()
#     time.sleep(5)
#     assert browser.current_url == 'https://www.saucedemo.com/v1/checkout-step-two.html', browser.current_url

def test_filters():
    test_auth_positive()
    time.sleep(3)
    browser.find_element(By.XPATH, "//*[@class='product_sort_container']").click()

    select_element = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    select = Select(select_element)
    select.select_by_value('az')
    time.sleep(2)
    select.select_by_value('za')
    time.sleep(2)
    select.select_by_value('lohi')
    time.sleep(2)
    select.select_by_value('hilo')

    # browser.quit()



#test_shopping_cart()
#test_item_page()
#test_placing_order()
test_filters()