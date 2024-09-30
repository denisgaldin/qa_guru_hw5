import pytest
from selene import browser
from selenium  import webdriver


@pytest.fixture
def set_browser_size():
    browser.driver.set_window_size(1920, 1080)


@pytest.fixture
def setup_browser(set_browser_size):
    browser.open('https://demoqa.com/automation-practice-form')

    yield browser
