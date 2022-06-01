# Library for solve_quiz_and_get_code
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
import math
# Libraries for a method that checks that an element does not appear on the page within a given time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=5):  # Constructor is a method that is called when we create an object.
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # The open method opens the desired page in the browser using the get() method
    def open(self):
        self.browser.get(self.url)

    # Method for calculating the mathematical expression and entering the answer
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

    # Method that checks that the element does not appear on the page for a given time
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # Method to check if some element disappears, should be used with an explicit wait
    # and with the until_not function, depending on what result we expect
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Exception handling construct
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Checking the transition to the login page
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    # Check if there is a login link
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # Method for go to cart
    def go_to_basket(self):
        button_see_basket = self.browser.find_element(*BasePageLocators.BUTTON_SEE_BASKET)
        button_see_basket.click()

    # Check if the user is logged in
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
