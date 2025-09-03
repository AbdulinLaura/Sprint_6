from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_scooter_logo(driver):
    page = MainPage(driver)
    page.open()
    driver.get(page.URL + "order")  # переходим на /order
    driver.find_element(By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR").click()
    assert driver.current_url.rstrip("/") == page.URL.rstrip("/")


def test_yandex_logo(driver):
    page = MainPage(driver)
    page.open()
    driver.find_element(By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI").click()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(EC.url_contains("dzen"))
    assert "dzen" in driver.current_url
