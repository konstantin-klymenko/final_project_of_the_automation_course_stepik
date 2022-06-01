from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # Checking the negative scenario
    LOGIN_LINK_INVALID = (By.XPATH, "//a[text()='Offers']")
    # Button for transit to basket
    BUTTON_SEE_BASKET = (By.CSS_SELECTOR, "span.btn-group a")
    # Icon if the user has successfully registered
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    # Items that will be available if the product is in the cart
    TEXT_WHEN_PRODUCT_IS_IN_BASKET = (By.CSS_SELECTOR, "div.row h2.col-sm-6")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "img.thumbnail")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    # Find email field
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    # Password field
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    # Confirm password field
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")


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




