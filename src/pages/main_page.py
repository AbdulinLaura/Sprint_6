from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    COOKIE_BTN_ID = (By.ID, "rcc-confirm-button")
    COOKIE_BTN_CLASS = (By.CLASS_NAME, "App_CookieButton__3cvqF")

    def open(self):
        self.open_url(self.URL)

    def accept_cookies(self):
        for loc in (self.COOKIE_BTN_ID, self.COOKIE_BTN_CLASS):
            try:
                self.click(loc)
                return True
            except Exception:
                pass
        return False

    @staticmethod
    def faq_question(number):
        return By.ID, f"accordion__heading-{number}"

    @staticmethod
    def faq_answer(number):
        return By.XPATH, f'//div[@id="accordion__panel-{number}"]//..//p'

    @staticmethod
    def order_button_top():
        return By.XPATH, "(//button[text()='Заказать'])[1]"

    @staticmethod
    def order_button_bottom():
        return By.XPATH, "(//button[text()='Заказать'])[2]"

