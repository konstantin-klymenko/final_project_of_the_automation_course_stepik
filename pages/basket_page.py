from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def guest_cant_see_text_if_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.TEXT_WHEN_PRODUCT_IS_IN_BASKET), \
            "Basket isn`t empty"

    def guest_cant_see_product_if_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Basket isn`t empty"