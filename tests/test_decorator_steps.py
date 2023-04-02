import allure
from selene import by, be
from selene.support.shared.jquery_style import s


def test_github(open_browser):
    click_input()
    enter_text('eroshenkoam/allure-example')
    submit_form()
    go_to_link('eroshenkoam/allure-example')
    go_to_issue()
    assert_visible_text('#76')


@allure.step("Клик по полю поиска")
def click_input():
    s(".header-search-input").click()


@allure.step("Ввод поискового запроса")
def enter_text(text):
    s(".header-search-input").send_keys(text)  # 'eroshenkoam/allure-example'


@allure.step("Отправка поискового запроса")
def submit_form():
    s(".header-search-input").submit()


@allure.step("Переход по ссылке")
def go_to_link(text):
    s(by.link_text(text)).click()


@allure.step("переход на вкладку issues")
def go_to_issue():
    s(by.id('issues-tab')).click()


@allure.step("Проверка наличия issue по тексту {text}")
def assert_visible_text(text):
    s(by.partial_text(text)).should(be.visible)
