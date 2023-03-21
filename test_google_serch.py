from selene.support.shared import browser
from selene import have


def test_search_selene(browser_preparation):
    assert browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_selene_negative(browser_preparation):
    assert browser.element('[id="search"]').should(have.text('Wrong request'))
