from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_backet()
    page.switch_to_alert()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.get_text_if_product_added()
