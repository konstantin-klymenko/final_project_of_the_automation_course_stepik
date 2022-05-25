from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException #Библиотека для обработки исключений

class ProductPage(BasePage):

    def add_product_to_backet(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def switch_to_alert(self):
        alert = self.browser.switch_to.alert

    #Check prodact name in basket
    def get_text_if_product_added(self):
        text1_add = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADD_BASKET)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        text1 = text1_add.text
        product = product_name.text
        assert text1 == product, "product not added"

    #Сheck price in basket
    def get_price_if_product_added(self):
        product_price_add = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_in_basket = product_price_add.text
        price = product_price.text
        assert price_in_basket == price, "product not added"


    #Конструкция для обработки исключений
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


