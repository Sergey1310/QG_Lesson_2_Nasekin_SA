from selene.support.shared import browser
from selene import have, be


def test_search_selene(browser_preparation):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_selene_negative(browser_preparation):
    browser.element('[name="q"]').should(be.blank).type('mfhdjkghjkghfgjkfhgjkfsgjnksfdgfg').press_enter()
    assert browser.element('.card-section').should(have.text('По запросу mfhdjkghjkghfgjkfhgjkfsgjnksfdgfg ничего не найдено'))
