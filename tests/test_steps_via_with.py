import allure
from selene import browser, by, be


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Ищем eroshenkoam/allure-example"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step("Переходим нв страницу eroshenkoam/allure-example"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем табу с Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем что элемент с текстом #76 виден"):
        browser.element(by.partial_text("#76")).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("/")

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys(repo)
    browser.element("#query-builder-test").submit()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()

@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)


