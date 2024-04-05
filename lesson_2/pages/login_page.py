from lesson_2.locators.login_locators import LoginLocators
from lesson_2.pages.base_page import BasePage
from lesson_2.src.user_data import UserData


class LoginPage(BasePage):
    locators = LoginLocators()
    user = UserData()
    
    def login(self):
        self.driver.find_element(*self.locators.USER_NAME).send_keys(self.user.standart_user_name)
        self.driver.find_element(*self.locators.PASSWORD).send_keys(self.user.password)
        self.driver.find_element(*self.locators.LOGIN).click()

