import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_configs():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    browser.config.driver_options = options

    yield

    browser.quit()

