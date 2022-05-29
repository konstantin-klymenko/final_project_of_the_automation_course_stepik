from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def switch_to_alert(self):
        alert = self.browser.switch_to.alert

    # Check product name in basket
    def get_text_if_product_added(self):
        text1_add = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADD_BASKET)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        text1 = text1_add.text
        product = product_name.text
        assert text1 == product, "product not added"

    # Сheck price in basket
    def get_price_if_product_added(self):
        product_price_add = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_in_basket = product_price_add.text
        price = product_price.text
        assert price_in_basket == price, "product not added"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_AFTER_ADD_BASKET), \
            "Success message is presented, but should not be"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_AFTER_ADD_BASKET), \
            "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_AFTER_ADD_BASKET), \
            "Success message is not disappeared, but should disappeared"

    def guest_cant_see_text_if_basket_empty(self):
        assert self.is_not_element_present(*ProductPageLocators.TEXT_WHEN_PRODUCT_IS_IN_BASKET), \
            "Basket isn`t empty"

    def guest_cant_see_product_if_basket_empty(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET), \
            "Basket isn`t empty"












