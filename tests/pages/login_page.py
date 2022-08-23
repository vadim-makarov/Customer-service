from tests.pages.base_page import BasePage
from tests.pages.locators import LoginPageLocators

LOGIN_LINK = 'http://127.0.0.1:5000/auth/login'


class LoginPage(BasePage):
    LOGIN = 'VadimM'
    PHONE = '+79022513250'

    def should_be_login_page(self):
        self.should_be_some_page()
        self.should_be_login_form_name()
        self.should_be_login_form_phone()
        self.should_be_register_link()

    def should_be_login_form_name(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_NAME), 'Login form_name is not presented'

    def should_be_login_form_phone(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM_PHONE_NUMBER), 'Login form_phone is not presented'

    def should_be_register_link(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_TO_REG_PAGE), 'Reg link is not presented'

    def login_user(self, name: str, phone: str):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_NAME).send_keys(name)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PHONE_NUMBER).send_keys(phone)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_SUBMIT).click()
