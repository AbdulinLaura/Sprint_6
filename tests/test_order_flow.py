import allure
import pytest
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage

from src.data.test_data import ORDER_DATA


class TestOrderFlow:
    @allure.title("Позитивный заказ — вход через верхнюю кнопку «Заказать»")
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_positive_order_from_top(self, driver, data):
        main = MainPage(driver)
        main.open()
        main.accept_cookies()
        main.click_top_order()

        order = OrderPage(driver)
        order.fill_first_page(data["name"], data["surname"], data["address"], data["metro"], data["phone"])
        order.fill_second_page(data["date"], data["rent"])
        order.confirm_order()
        assert order.is_success_visible()

    @allure.title("Позитивный заказ — вход через нижнюю кнопку «Заказать»")
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_positive_order_from_bottom(self, driver, data):
        main = MainPage(driver)
        main.open()
        main.accept_cookies()
        main.click_bottom_order()

        order = OrderPage(driver)
        order.fill_first_page(data["name"], data["surname"], data["address"], data["metro"], data["phone"])
        order.fill_second_page(data["date"], data["rent"])
        order.confirm_order()
        assert order.is_success_visible()
