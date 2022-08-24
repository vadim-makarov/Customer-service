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
    SMS_CODE_FORM = (By.ID, 'code_input')
    SMS_CONFIRM = (By.CSS_SELECTOR, 'body > main > main > div > div > div > form > div > div.d-grid.gap-2.col-6.mx-auto > div > button.btn.btn-warning')
    SMS_RESEND = (By.ID, 'BtnCounter')
    SMS_ALERT_CODE = (By.CSS_SELECTOR, 'body > div')
class LoginPageLocators(MainPageLocators):
    LOGIN_FORM_NAME = (By.ID, 'username')
    LOGIN_FORM_PHONE_NUMBER = (By.ID, 'phone_number')
    LOGIN_FORM_SUBMIT = (By.ID, 'submit')
    LOGIN_FORM_TO_REG_PAGE = (By.CSS_SELECTOR, 'body > main > main > div > div > div > div > a')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'body > header > div > div > div > button')
    LOGOUT_LINK_MODAL = (By.CSS_SELECTOR, '#logoutModal > div > div > div.modal-footer > a')
