import pytest
import time
from lesson_2.pages.order_page import OrderPage
from lesson_2.src.order_data import OrderData
from lesson_2.src.urls import Urls


class TestOrder:
    url = Urls()
    
    @pytest.mark.parametrize("data", OrderData.user_data)
    def test_order_without_credential(self, driver, data):
        page = OrderPage(driver, self.url.base_url)
        err = page.order_without_credential(data)
        assert err == data[3]
        #time.sleep(5)
