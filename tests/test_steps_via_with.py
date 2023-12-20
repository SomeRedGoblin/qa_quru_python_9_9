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
