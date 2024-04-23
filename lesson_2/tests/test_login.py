import pytest
import time
from lesson_2.locators.main_page_locators import MainPage_Locators
from lesson_2.pages.login_page import LoginPage
from lesson_2.src.urls import Urls
import allure

@allure.epic("Testing login page")
# From login_page.py file calling LoginPage class
class TestLogin:
    url = Urls()
    main_locators = MainPage_Locators()
    
    @allure.title("test positive login")
    @allure.description("Test checks the actual title when the user lands on the home page")

    # if the user is not logger then the page will not work
    @allure.severity(allure.severity_level.BLOCKER) 
    def test_login_positive(self, driver):
        page = LoginPage(driver, self.url.base_url)
    
        # Checking the actual title of the home page
        actual_title = page.get_text(self.main_locators.TITLE)
        expected_title = "Products"
        assert actual_title == expected_title, \
            f"Unexpected text, expected text: {expected_title},actual text: {actual_title} "

    @allure.title("test login number of cards")
    @allure.description("Test checks the actual title when the user lands on the home page and see all cards of store products")
    @allure.severity(allure.severity_level.BLOCKER) 
    
    def test_login_len_cards(self, driver):
        page = LoginPage(driver, self.url.base_url)

        # Checking the number of items on the main page
        expected_len = 6
        cards = page.get_length(self.main_locators.INVENTORY_ITEMS)
        assert cards == expected_len, f"Expected: {expected_len}, actual: {cards}"
        #time.sleep(3)

    # print number of all card products
    @pytest.mark.parametrize("value", range(1, 7))
    def test_check_cards(self, driver, value):
        page = LoginPage(driver, self.url.base_url)
        locator = page.check_card(value)
        print(locator)
        