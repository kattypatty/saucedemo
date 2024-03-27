import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Chrome()
browser.implicitly_wait(2)

@pytest.fixture
def auth():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', browser.current_url

def test_auth_with_incorrect_data(auth):
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/', browser.current_url

def test_shopping_cart(auth):
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

def test_item_page(auth):
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html'

    # On invenroty page, click on item image and page successfully transfers
    browser.find_elements(By.XPATH, "//*[@id='item_4_img_link']/img")[0].click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4', browser.current_url
    
    # On image page, click on "back" button to come back to the inventory page
    browser.find_element(By.XPATH, "//*[@class='inventory_details_back_button']").click()

    # On invenroty page, click on a product name and page successfully transfers 
    browser.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4', browser.current_url

def test_placing_order(auth):
    # On inventory page, click on "Add to cart" button.
    browser.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']").click()

    # On inventory page, click on the cart.
    browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

    # On an item page, click on "checkout" button and page successfully transfers 
    browser.find_element(By.XPATH, "//*[@class='btn_action checkout_button']").click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html', browser.current_url
    
    # Placing customer details in the checkout info
    browser.find_element('xpath', "//*[@id='first-name']").send_keys('Vasya')
    browser.find_element('xpath', "//*[@id='last-name']").send_keys('Petrov')
    browser.find_element('xpath', "//*[@id='postal-code']").send_keys('98660')

    # On checkout information page, click on "continue" button and page successfully transfers
    browser.find_element(By.XPATH, "//*[@class='btn_primary cart_button']").click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/checkout-step-two.html', browser.current_url

def test_filters(auth):
    # On inventory page, click on "product_sort_container" drop down menu
    browser.find_element(By.XPATH, "//*[@class='product_sort_container']").click()

    # On inventory page, select from drop down menu:
    # a to z filter
    # z to a filter
    # low to high filter
    # high to low filter
    select_element = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    select = Select(select_element)
    select.select_by_value('az')
    select.select_by_value('za')
    select.select_by_value('lohi')
    select.select_by_value('hilo')

def test_burger_menu_logout(auth):
    # On inventory page, click on "burger button" and side bar will appear
    browser.find_element(By.XPATH, "//*[@class='bm-burger-button']").click()

    # Click on "Logout" button in menu
    browser.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()

    # The login page appeared successfully
    assert browser.current_url == 'https://www.saucedemo.com/v1/index.html', browser.current_url

def test_burger_menu_about(auth):
    # On inventory page, click on "burger button" and side bar will appear
    browser.find_element(By.XPATH, "//*[@class='bm-burger-button']").click()

    # Click on "About" button in menu and page successfully transfers
    browser.find_element(By.XPATH, "//*[@id='about_sidebar_link']").click()
    assert browser.current_url == 'https://saucelabs.com/', browser.current_url

def test_reset_app_state(auth):
    # On inventory page, click on "Add to cart" button.
    browser.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']").click()

    # On inventory page, click on the shopping cart.
    browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

    # On inventory page, click on "burger button" and side bar will appear
    browser.find_element(By.XPATH, "//*[@class='bm-burger-button']").click()
    
    # Click on "Reset App State" button in menu and removes items from shopping cart
    browser.find_element(By.XPATH, "//*[@id='reset_sidebar_link']").click()

    # Checking if the shoppig card is empty
    try:
        browser.find_element(By.XPATH, "//*[@class='fa-layers-counter shopping_cart_badge']")
        assert False, "Shopping cart should be empty."
    except NoSuchElementException:
        pass    

#test_auth_with_incorrect_data()
#test_shopping_cart()
#test_item_page()
#test_placing_order()
#test_filters()
#test_burger_menu_logout()
#test_burger_menu_about()
#test_reset_app_state()


