from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page_when_it_is_empty(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)  # Инициализируем LoginPage в теле теста
    basket_page.guest_cant_see_product_if_basket_empty()
    basket_page.guest_cant_see_text_if_basket_empty()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/da/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()  # Тянет с base_page

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.switch_to_alert()
        page.solve_quiz_and_get_code()
        page.get_text_if_product_added()
        page.get_price_if_product_added()

    def test_user_cant_see_success_message(self, browser):
        # Товар Coders at Work
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)  # Инициализируем LoginPage в теле теста
    login_page.should_be_login_form()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/\
?promo=newYear2019",
                                  "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/\
?promo=newYear"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.switch_to_alert()
    page.solve_quiz_and_get_code()
    page.get_text_if_product_added()
    page.get_price_if_product_added()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# Негативный тест о том что пользователь не должен видеть сообщение об успешном добавлении товара в корзину
@pytest.mark.neg
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Товар Coders at Work
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.switch_to_alert()
    page.solve_quiz_and_get_code()
    page.guest_cant_see_success_message_after_adding_product_to_basket()


# Пользователь не должен видеть сообщение об успешном добавлении товара в корзину так как он его не добавил
def test_guest_cant_see_success_message(browser):
    # Товар Coders at Work
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()


# Негативный тест сообщение об успешном добавлении товара в корзину должно пропасть после добавления товара
@pytest.mark.neg
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Товар Coders at Work
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.switch_to_alert()
    page.solve_quiz_and_get_code()
    page.message_disappeared_after_adding_product_to_basket()


# Клиент может добавить акционный продукт в корзину (ссылка содержит дополнение "?promo=offerN")
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param
                                  ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                                                                            marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_promo(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.switch_to_alert()
    page.solve_quiz_and_get_code()
    page.get_text_if_product_added()
    page.get_price_if_product_added()




