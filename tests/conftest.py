import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import config
from selene import browser
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_configs():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 4.0
    config.window_width = 1920
    config.window_height = 1080
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


