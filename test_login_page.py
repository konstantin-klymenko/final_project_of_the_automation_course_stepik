import time

from .pages.login_page import LoginPage
import pytest

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

@pytest.mark.new
def test_register_new_user(browser):
    link = "http://selenium1py.pythonanywhere.com/da/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user()
    time.sleep(6)
    page.register_new_user_assert()
