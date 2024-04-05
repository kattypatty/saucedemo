import time
from lesson_2.locators.main_page_locators import MainPage_Locators
from lesson_2.pages.login_page import LoginPage
from lesson_2.src.urls import Urls

# From login_page.py file calling LoginPage class
class TestLogin:
    url = Urls()
    main_locators = MainPage_Locators()
    
    def test_login_positive(self, driver): 
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()

        # Checking the actual title of the home page
        actual_title = page.get_text(self.main_locators.TITLE)
        expected_title = "Products"
        assert actual_title == expected_title, \
            f"Unexpected text, expected text: {expected_title},actual text: {actual_title} "

    def test_login_len_cards(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()

        # Checking the number of items on the main page
        expected_len = 6
        cards = page.get_lenght(self.main_locators.INVENTORY_ITEMS)
        assert cards == expected_len, f"Expected: {expected_len}, actual: {cards}"
        time.sleep(3)


