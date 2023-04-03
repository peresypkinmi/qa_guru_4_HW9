from selene import by, be
from selene.support.shared.jquery_style import s


def test_github(open_browser):
    s(".header-search-input").click()
    s(".header-search-input").send_keys('peresypkinmi/qa_guru_4_HW9')
    s(".header-search-input").submit()
    s(by.link_text('peresypkinmi/qa_guru_4_HW9')).click()
    s(by.id('issues-tab')).click()
    s(by.partial_text('#1')).should(be.visible)
