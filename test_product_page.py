from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    #Товар Coders at Work
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #Товар The shellcoder's handbook
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_backet()
    page.switch_to_alert()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.get_text_if_product_added()
    page.get_price_if_product_added()

