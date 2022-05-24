from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK = (By.XPATH, "//a[text()='Offers']") #Проверка негативного сценария
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    #Button for add product to the backet
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    TEXT1 = (By.XPATH, "//strong[contains(text(), \"The shellcoder's handbook\")]")
    TEXT2 = (By.XPATH, "//strong[contains(text(), \"Deferred benefit offer\")]")


