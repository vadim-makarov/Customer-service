from tests.pages.base_page import BasePage
from tests.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    NAME = 'VadimM'
    PHONE = '+79022513250'

    def should_be_login_page(self):
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

    def login_user(self, name: str = NAME, phone: str = PHONE):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_NAME).send_keys(name)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PHONE_NUMBER).send_keys(phone)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_SUBMIT).click()

    def user_should_be_log_on(self):
        assert self.NAME in self.browser.find_element(*LoginPageLocators.LOGIN_LINK).text, 'User is not logged in!'

    def guest_should_not_be_log_on(self):
        assert 'Log in' in self.browser.find_element(*LoginPageLocators.LOGIN_LINK).text, 'Guest is not logged in!'

    def user_can_see_logout_link(self):
        assert self.browser.find_element(*LoginPageLocators.LOGOUT_LINK), 'Logout link is not presented'

    def user_can_see_logout_modal(self):
        self.browser.find_element(*LoginPageLocators.LOGOUT_LINK).click()
        assert self.browser.find_element(*LoginPageLocators.LOGOUT_LINK_MODAL), 'Logout modal is not presented'

    def user_can_log_out(self):
        self.browser.find_element(*LoginPageLocators.LOGOUT_LINK).click()
        self.browser.find_element(*LoginPageLocators.LOGOUT_LINK_MODAL).click()
