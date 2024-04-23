import pytest
import time
from lesson_2.pages.order_page import OrderPage
from lesson_2.src.order_data import OrderData
from lesson_2.src.urls import Urls

class TestOrder:
    url = Urls()
    data = OrderData()

    def test_order_with_valid_credential(self, driver):
        page = OrderPage(driver, self.url.base_url)
        expected_text = page.order_with_valid_credential(self.data.user_data_with_valid_credential)
        assert self.data.successful_message == expected_text,\
            f"Unexpected text, expected text: {expected_text}, actual text: {self.data.successful_message}"

    @pytest.mark.parametrize("data", data.user_data_with_invalid_credential)
    def test_order_with_invalid_credential(self, driver, data):
        page = OrderPage(driver, self.url.base_url)
        err = page.order_with_invalid_credential(data)

        # Comparison of error message text on the website with what we get
        assert err == data[3]
        #time.sleep(5)

   