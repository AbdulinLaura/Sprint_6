from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
import allure


class OrderPage(BasePage):
    FIELD_NAME = (By.CSS_SELECTOR, "input[placeholder*='Имя']")
    FIELD_SURNAME = (By.CSS_SELECTOR, "input[placeholder*='Фамил']")
    FIELD_ADDRESS = (By.CSS_SELECTOR, "input[placeholder*='Адрес']")
    FIELD_METRO = (By.CSS_SELECTOR, "input[placeholder*='Станция метро']")
    FIELD_PHONE = (By.CSS_SELECTOR, "input[placeholder*='Телефон']")
    NEXT_BTN = (By.XPATH, "//button[normalize-space()='Далее']")

    FIELD_DATE = (By.CSS_SELECTOR, "input[placeholder*='Когда']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-root")
    ORDER_SUBMIT = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[normalize-space()='Заказать']")
    COLOR_BLACK = (By.ID, "black")

    HEADER_STEP1 = (By.XPATH, "//*[contains(text(),'Для кого самокат')]")
    HEADER_STEP2 = (By.XPATH, "//*[contains(text(),'Про аренду')]")
    BACK_BTN = (By.XPATH, "//button[normalize-space()='Назад']")

    CONFIRM_MODAL = (By.XPATH, "//div[contains(@class,'Order_Modal__')]")
    MODAL_YES = (By.XPATH, "//div[contains(@class,'Order_Modal__')]//button[normalize-space()='Да']")
    MODAL_SUCCESS = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]")

    @allure.step("Гарантируем, что открыт шаг 1 формы (при необходимости нажимаем «Назад»)")
    def ensure_step1(self):
        if self.is_visible(self.HEADER_STEP2) and not self.is_visible(self.FIELD_PHONE):
            self.click(self.BACK_BTN)
        self.wait_visible(self.FIELD_PHONE)

    @allure.step("Заполняем шаг 1: Имя={name}, Фамилия={surname}, Адрес={address}, Метро={metro}, Телефон={phone}")
    def fill_first_page(self, name, surname, address, metro, phone):
        self.ensure_step1()
        self.type(self.FIELD_NAME, name)
        self.type(self.FIELD_SURNAME, surname)
        self.type(self.FIELD_ADDRESS, address)
        self.type(self.FIELD_METRO, metro)
        self.press_keys(self.FIELD_METRO, Keys.ARROW_DOWN, Keys.ENTER)
        self.type(self.FIELD_PHONE, phone)
        self.click(self.NEXT_BTN)

    @allure.step("Заполняем шаг 2: Дата={date}, Срок аренды={rent} (выбираем цвет при необходимости)")
    def fill_second_page(self, date, rent):
        self.type(self.FIELD_DATE, date)
        self.press_keys(self.FIELD_DATE, Keys.ENTER)  # закрыть календарь
        self.click(self.RENT_DROPDOWN)
        self.click((By.XPATH, f"//div[normalize-space()='{rent}']"))
        self.click(self.COLOR_BLACK)

    @allure.step("Подтверждаем заказ: «Заказать» → «Да»")
    def confirm_order(self):
        self.wait_clickable(self.ORDER_SUBMIT)
        self.click(self.ORDER_SUBMIT)
        self.wait_visible(self.CONFIRM_MODAL)
        self.wait_clickable(self.MODAL_YES)
        self.click(self.MODAL_YES)

    @allure.step("Проверяем всплывающее окно об успешном оформлении")
    def is_success_visible(self) -> bool:
        try:
            self.wait_visible(self.MODAL_SUCCESS)
            return True
        except TimeoutException:
            return False
