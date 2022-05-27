from selenium.common.exceptions import NoAlertPresentException  # Библиотека для  solve_quiz_and_get_code
import math
from selenium.common.exceptions import NoSuchElementException  # Библиотека для обработки исключений
from .locators import MainPageLocators  # Импорт локаторов для методов (go_to_login_page и should_be_login_link)

# Библиотеки для метода, который проверяет, что элемент не появляется на странице в течение заданного времени
from selenium.common.exceptions import TimeoutException  # Библиотека для обработки исключений
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
########################################################################################################################
class BasePage():
    def __init__(self, browser, url, timeout=5):  # конструктор — метод, который вызывается, когда мы создаем объект.
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
########################################################################################################################
    # метод open открывает нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)
########################################################################################################################
    # Метод для подсчета математического выражения и ввода ответа для test_product_page.py
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
########################################################################################################################
    # метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
########################################################################################################################
    # Метод для проверки, что какой-то элемент исчезает, его следует применять с явным ожиданием
    # и с функцией until_not, в зависимости от того, какой результат мы ожидаем
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
########################################################################################################################
    # Конструкция для обработки исключений
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
########################################################################################################################
    # Проверка перехода на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    # Проверка наличия ссылки для логина
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
