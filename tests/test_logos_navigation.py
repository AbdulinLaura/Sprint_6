import allure

from src.data.test_data import BASE_URL
from src.pages.main_page import MainPage


class TestLogosNavigation:
    @allure.title("Тест: клик по лого Самоката ведёт на главную")
    def test_scooter_logo(self, driver):
        page = MainPage(driver)
        page.open()
        page.accept_cookies()

        page.open_order()
        page.click_scooter_logo()

        assert page.current_url().rstrip("/") == BASE_URL.rstrip("/"), "После клика по лого Самоката не попали на главную страницу"

    @allure.title("Тест: клик по лого Яндекса открывает Dzen в новой вкладке")
    def test_yandex_logo(self, driver):
        page = MainPage(driver)
        page.open()
        page.accept_cookies()

        page.click_yandex_logo()
        page.wait_number_of_windows(2)
        page.switch_to_last_window()
        page.wait_url_contains("dzen")

        assert "dzen" in page.current_url(), "После клика по лого Яндекса не открылась главная страница Дзена"
