from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException #Библиотека для обработки исключений
from .locators import MainPageLocators


class MainPage(BasePage):
    # Проверка перехода на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    #Проверка наличия ссылки для логина
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    # Конструкция для обработки исключений
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True