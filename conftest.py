import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_setup():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1000
    browser.config.window_height = 1000


@pytest.fixture()
def browser_preparation(browser_setup):
    browser.open('https://google.com')
