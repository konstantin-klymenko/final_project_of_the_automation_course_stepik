from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException #Библиотека для обработки исключений

class ProductPage(BasePage):

    def add_product_to_backet(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def switch_to_alert(self):
        alert = self.browser.switch_to.alert


    def get_text_if_product_added(self):
        text1_add = self.browser.find_element(*ProductPageLocators.TEXT1)
        text1_compare = text1_add.text
        assert "The shellcoder's handbook" == text1_compare, "product not added"
        text2_add = self.browser.find_element(*ProductPageLocators.TEXT2)
        text2_compare = text2_add.text
        assert "Deferred benefit offer" == text2_compare, "product not added"



    #Конструкция для обработки исключений
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


