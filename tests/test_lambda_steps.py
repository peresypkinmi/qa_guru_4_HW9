import allure
from selene import by, be
from selene.support.shared.jquery_style import s


def test_github(open_browser):
    with allure.step("Клик по полю поиска"):
        s(".header-search-input").click()

    with allure.step("Ввод поискового запроса"):
        s(".header-search-input").send_keys('peresypkinmi/qa_guru_4_HW9')

    with allure.step("Отправка поискового запроса"):
        s(".header-search-input").submit()

    with allure.step("Переход по ссылке"):
        s(by.link_text('peresypkinmi/qa_guru_4_HW9')).click()

    with allure.step("переход на вкладку issues"):
        s(by.id('issues-tab')).click()

    with allure.step("Проверка наличия issue по тексту '#1'"):
        s(by.partial_text('#1')).should(be.visible)
