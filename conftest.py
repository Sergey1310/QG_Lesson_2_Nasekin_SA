import pytest
from selene import browser, be


@pytest.fixture(scope="session")
def browser_setup():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1000
    browser.config.window_height = 1000


@pytest.fixture()
def browser_preparation(browser_setup):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
