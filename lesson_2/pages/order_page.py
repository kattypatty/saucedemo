
from lesson_2.locators.cart_locators import CartLocators
from lesson_2.locators.main_page_locators import MainPage_Locators
from lesson_2.locators.order_locators import OrderLocators
from lesson_2.pages.base_page import BasePage


class OrderPage(BasePage):
    order_locators = OrderLocators()
    main_locators = MainPage_Locators()
    cart_locators = CartLocators()

    def order_without_credential(self, lst_data):
        self.add_item_to_cart()
        self.fill_fields(lst_data[0], lst_data[1], lst_data[2])
        return self.get_text(self.order_locators.ERROR_MESSAGE)

    def add_item_to_cart(self):
        self.element_is_clickable(self.main_locators.SAUCE_LABS_BACKPACK).click()
        self.element_is_clickable(self.main_locators.CART_BTN).click()
        self.element_is_clickable(self.cart_locators.CHECKOUT_BTN).click()

    def fill_fields(self, first_name, last_name, zip_code):
        self.element_is_visible(self.order_locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.order_locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.order_locators.ZIP_CODE).send_keys(zip_code)
        self.element_is_clickable(self.order_locators.CONTINUE_BTN).click()



