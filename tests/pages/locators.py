from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > a')
    FEATURES_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > ul > li:nth-child(1) > a')
    PRICING_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > ul > li:nth-child(2) > a')
    REVIEWS_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > ul > li:nth-child(3) > a')
    LOGIN_LINK = (By.CSS_SELECTOR, "body > header > div > div > div > a.btn.btn-outline-light.me-2")
    REGISTER_LINK = (By.CSS_SELECTOR, 'body > header > div > div > div > a.btn.btn-warning')


class RegisterPageLocators(MainPageLocators):
    REGISTER_FORM_NAME = (By.ID, 'username')
    REGISTER_FORM_PHONE_NUMBER = (By.ID, 'phone_number')
    REGISTER_FORM_SEND_SMS = (By.ID, 'confirm')


class LoginPageLocators(MainPageLocators):
    LOGIN_FORM_NAME = (By.ID, 'username')
    LOGIN_FORM_PHONE_NUMBER = (By.ID, 'phone_number')
    LOGIN_FORM_SUBMIT = (By.ID, 'submit')
    LOGIN_FORM_TO_REG_PAGE = (By.CSS_SELECTOR, 'body > main > main > div > div > div > div > a')


class ProductPageLocators(MainPageLocators):
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    TITLE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    BASKET_TITLE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    BASKET_PRICE = (
        By.CSS_SELECTOR,
        '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')
