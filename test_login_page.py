from .pages.login_page import LoginPage


def test_should_be_login_url_on_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/da/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_should_be_registration_form(browser):
    link = "http://selenium1py.pythonanywhere.com/da/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()