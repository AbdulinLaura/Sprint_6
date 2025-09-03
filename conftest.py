import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("APP_BASE_URL", "https://qa-scooter.praktikum-services.ru/")


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("-headless")  # для безголового режима
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
