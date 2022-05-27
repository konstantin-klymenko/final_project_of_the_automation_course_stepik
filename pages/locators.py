from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.XPATH, "//a[text()='Offers']") #Проверка негативного сценария
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    # Button for add product to the basket
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    # Product name on product page
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    # Product price on product page
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div > p.price_color")
    # Product name on the message after adding product to the basket
    PRODUCT_NAME_AFTER_ADD_BASKET = (By.CSS_SELECTOR, "div#messages .alert:nth-child(1) strong")
    # Product price on the message after adding product to the basket
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner p:nth-child(1) strong")




