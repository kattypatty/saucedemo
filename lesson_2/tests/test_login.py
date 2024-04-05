import time
from lesson_2.pages.login_page import LoginPage
from lesson_2.src.urls import Urls

class TestLogin():
    url = Urls()
    def test_login_positive(self, driver): 
        page = LoginPage(driver, self.url.base_url)

# Checking the actual title of the main page
        actual_title = driver.find_element(*TITLE).text
        expected_title = "Products"
        assert actual_title == expected_title, f"Unexpected text, expected text: {expected_title},actual text: {actual_title} "

# Checking the number of items on the main page
        items_list = driver.find_elements(*INVENTORY_ITEMS)
        expected_items = 6
        assert len(items_list) == expected_items, f"Expected: {expected_items}, actual: {len(items_list)}"
        time.sleep(3)

def test_login_negative(self, driver):
# Wrong username
    assert driver.title == "Swag Labs"
    assert driver.find_element("css selector", 'h3').text == "Epic sadface: Sorry, this user"
