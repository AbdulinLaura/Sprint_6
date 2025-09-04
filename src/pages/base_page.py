from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url: str):
        self.driver.get(url)

    def current_url(self) -> str:
        return self.driver.current_url

    def wait_url_contains(self, text: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_number_of_windows(self, n: int, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(n))

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def is_visible(self, locator, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def scroll_into_view(self, el, offset: int = -80):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        if offset:
            self.driver.execute_script(f"window.scrollBy(0, {offset});")

    def click(self, locator):
        el = self.wait_present(locator)
        self.scroll_into_view(el)
        try:
            self.wait_clickable(locator).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)

    def click_webelement(self, el):
        self.scroll_into_view(el)
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)

    def get_text(self, locator) -> str:
        return self.wait_visible(locator).text

    def type(self, locator, text: str, clear: bool = False):
        el = self.wait_present(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    def press_keys(self, locator, *keys):
        el = self.wait.until(EC.presence_of_element_located(locator))
        for k in keys:
            el.send_keys(k)
