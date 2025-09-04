import logging

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    logging.warning("privet andrei!!!")
    yield driver
    driver.quit()
