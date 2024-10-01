import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture
def set_browser_size():
    browser.driver.set_window_size(1920, 1080)


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/'
    driver_options = webdriver.ChromeOptions()
    #driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options

    yield

    browser.quit()