from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest

from lesson_2.locators.login_locators import LoginLocators
from lesson_2.locators.main_page_locators import MainPage_Locators
from lesson_2.src.user_data import UserData


class BasePage:
    timeout = 10
    login_locators = LoginLocators()
    main_locators = MainPage_Locators()
    user = UserData()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        # opening webrowser
        self.open()
        # Authentication process to get access to website
        self.login()
    
    @allure.step("Login")
    def login(self):
        with allure.step("Username"):
            self.element_is_visible(self.locators.USER_NAME).send_keys(self.user.standart_user_name)
        with allure.step("Password"):   
            self.element_is_visible(self.locators.PASSWORD).send_keys(self.user.password)
        with allure.step("Click_Login_Button"):
            self.element_is_clickable(self.locators.LOGIN).click()

    @allure.step("Open browser")
    # opening webrowser
    def open(self):
        self.driver.get(self.url)

    @allure.step("Get text")
    # getting text to check the actual title of the home page
    def get_text(self, locator):
        return self.element_is_visible(locator).text

    @ allure.step("Get length")
    # getting the length or number of inventory cards on the home page
    def get_length(self, locator):
        return len(self.elements_are_visible(locator))
    
    # click on any button
    def click_on_element(self, locator):
        self.element_is_visible(locator).click()
    
    # checking an element is visible and enabled such that you can click it
    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    # waiting until the element becomes visible
    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    
    def check_card(self, value):
        self.main_locators.get_card(value=value)