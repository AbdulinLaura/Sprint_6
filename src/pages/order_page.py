from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage


class OrderPage(BasePage):
    # --- шаг 1 ---
    FIELD_NAME = (By.CSS_SELECTOR, "input[placeholder*='Имя']")
    FIELD_SURNAME = (By.CSS_SELECTOR, "input[placeholder*='Фамил']")
    FIELD_ADDRESS = (By.CSS_SELECTOR, "input[placeholder*='Адрес']")
    FIELD_METRO = (By.CSS_SELECTOR, "input[placeholder*='Станция метро']")
    FIELD_PHONE = (By.CSS_SELECTOR, "input[placeholder*='Телефон']")
    NEXT_BTN = (By.XPATH, "//button[normalize-space()='Далее']")

    # --- шаг 2 ---
    FIELD_DATE = (By.CSS_SELECTOR, "input[placeholder*='Когда']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-root")
    # КНОПКА «Заказать» ТОЛЬКО В БЛОКЕ КНОПОК ФОРМЫ, НЕ ИЗ ХЕДЕРА!
    ORDER_SUBMIT = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[normalize-space()='Заказать']")
    COLOR_BLACK = (By.ID, "black")

    # навигация/маркеры шагов
    HEADER_STEP1 = (By.XPATH, "//*[contains(text(),'Для кого самокат')]")
    HEADER_STEP2 = (By.XPATH, "//*[contains(text(),'Про аренду')]")
    BACK_BTN = (By.XPATH, "//button[normalize-space()='Назад']")

    # модалки
    CONFIRM_MODAL = (By.XPATH, "//div[contains(@class,'Order_Modal__')]")
    MODAL_YES = (By.XPATH, "//div[contains(@class,'Order_Modal__')]//button[normalize-space()='Да']")
    MODAL_SUCCESS = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]")

    def ensure_step1(self):
        if self.is_visible(self.HEADER_STEP2) and not self.is_visible(self.FIELD_PHONE):
            self.click(self.BACK_BTN)
        self.wait.until(EC.visibility_of_element_located(self.FIELD_PHONE))

    def fill_first_page(self, name, surname, address, metro, phone):
        self.ensure_step1()
        d = self.driver
        d.find_element(*self.FIELD_NAME).send_keys(name)
        d.find_element(*self.FIELD_SURNAME).send_keys(surname)
        d.find_element(*self.FIELD_ADDRESS).send_keys(address)
        d.find_element(*self.FIELD_METRO).send_keys(metro, Keys.ARROW_DOWN, Keys.ENTER)
        d.find_element(*self.FIELD_PHONE).send_keys(phone)
        d.find_element(*self.NEXT_BTN).click()

    def fill_second_page(self, date, rent):
        d = self.driver
        d.find_element(*self.FIELD_DATE).send_keys(date, Keys.ENTER)  # закрыть календарь
        d.find_element(*self.RENT_DROPDOWN).click()
        d.find_element(By.XPATH, f"//div[normalize-space()='{rent}']").click()
        try:
            d.find_element(*self.COLOR_BLACK).click()
        except Exception:
            pass

    def confirm_order(self):
        # жмём ИМЕННО кнопку из блока формы
        self.wait.until(EC.element_to_be_clickable(self.ORDER_SUBMIT))
        self.click(self.ORDER_SUBMIT)

        # дождаться появления модалки подтверждения и «Да»
        self.wait.until(EC.visibility_of_element_located(self.CONFIRM_MODAL))
        self.wait.until(EC.element_to_be_clickable(self.MODAL_YES))
        self.click(self.MODAL_YES)

    def is_success_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.MODAL_SUCCESS))
            return True
        except TimeoutException:
            return False
