import pytest
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage

from src.data.test_data import ORDER_DATA


@pytest.mark.parametrize("entry", ["top", "bottom"])
@pytest.mark.parametrize("data", ORDER_DATA)
def test_positive_order_for_each_entry(driver, data, entry):
    main = MainPage(driver)
    main.open()
    main.accept_cookies()

    if entry == "top":
        main.click(main.order_button_top())
    else:
        main.click(main.order_button_bottom())

    order = OrderPage(driver)
    order.fill_first_page(
        data["name"], data["surname"], data["address"], data["metro"], data["phone"]
    )
    order.fill_second_page(data["date"], data["rent"])
    order.confirm_order()

    assert order.is_success_visible()
