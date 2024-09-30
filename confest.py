import pytest
from selene import browser


@pytest.fixture
def set_browser_size():
    browser.driver.set_window_size(1920, 1080)


@pytest.fixture
def setup_browser(set_browser_size):
    browser.open('https://duckduckgo.com/')

    yield browser
