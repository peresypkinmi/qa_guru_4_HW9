from selene import by, be
from selene.support.shared.jquery_style import s


def test_github(open_browser):
    s(".header-search-input").click()
    s(".header-search-input").send_keys('eroshenkoam/allure-example')
    s(".header-search-input").submit()
    s(by.link_text('eroshenkoam/allure-example')).click()
    s(by.id('issues-tab')).click()
    s(by.partial_text('#76')).should(be.visible)
