from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

from ..data.test_data import BASE_URL


class MainPage(BasePage):
    ALL_ORDER_BTNS = (By.XPATH, "//button[normalize-space()='Заказать']")
    COOKIE_BTN_ID = (By.ID, "rcc-confirm-button")
    COOKIE_BTN_CLASS = (By.CLASS_NAME, "App_CookieButton__3cvqF")

    # ЛОГОТИПЫ
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")

    @allure.step("Открываем главную страницу")
    def open(self):
        self.open_url(BASE_URL)

    @allure.step("Открываем страницу заказа /order")
    def open_order(self):
        self.open_url(BASE_URL + "order")

    @allure.step("Принимаем cookies, если баннер виден")
    def accept_cookies(self):
        for loc in (self.COOKIE_BTN_ID, self.COOKIE_BTN_CLASS):
            try:
                self.click(loc)
                break
            except Exception:
                pass

    def faq_question(self, i):
        return (By.ID, f"accordion__heading-{i}")

    def faq_answer(self, i):
        return (By.ID, f"accordion__panel-{i}")

    @allure.step("Жмём верхнюю кнопку «Заказать»")
    def click_top_order(self):
        btns = self.driver.find_elements(*self.ALL_ORDER_BTNS)
        self.click_webelement(btns[0])

    @allure.step("Жмём нижнюю кнопку «Заказать»")
    def click_bottom_order(self):
        btns = self.driver.find_elements(*self.ALL_ORDER_BTNS)
        self.click_webelement(btns[-1])

    @allure.step("Кликаем по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
