from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def guest_cant_see_text_if_basket_empty(self):
        assert self.is_not_element_present(*MainPageLocators.TEXT_WHEN_PRODUCT_IS_IN_BASKET), \
            "Basket isn`t empty"

    def guest_cant_see_product_if_basket_empty(self):
        assert self.is_not_element_present(*MainPageLocators.PRODUCT_IN_BASKET), \
            "Basket isn`t empty"


