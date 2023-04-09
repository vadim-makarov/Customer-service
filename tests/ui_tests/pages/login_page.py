import random
import string

from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    NAME = ''.join(random.sample(string.ascii_lowercase, 5))
    PHONE = '+' + ''.join(random.sample(string.digits * 3, 11))

    def should_be_login_page(self):
        self.should_be_some_page(self.LOGIN_LINK)
        self.should_be_login_form_name()
        self.should_be_login_form_phone()
        self.should_be_element(LoginPageLocators.LOGIN_FORM_TO_REG_PAGE)

    def should_be_login_form_name(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_NAME), 'Login form_name is not presented'

    def should_be_login_form_phone(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM_PHONE_NUMBER), 'Login form_phone is not presented'

    def can_go_register_from_login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_TO_REG_PAGE).click()
        self.should_be_some_page('register')

    def user_should_be_logged_in(self):
        assert 'Log in' not in self.browser.find_element(*LoginPageLocators.LOGIN_LINK).text, 'User is not logged in!'

    def guest_should_not_be_logged_in(self):
        assert 'Log in' in self.browser.find_element(*LoginPageLocators.LOGIN_LINK).text, 'Guest is not logged in!'

    def user_can_see_logout_link(self):
        assert self.browser.find_element(*LoginPageLocators.LOGOUT_LINK), 'Logout link is not presented'

    def user_can_see_logout_modal(self):
        self.browser.find_element(*LoginPageLocators.LOGOUT_LINK).click()
        assert self.browser.find_element(*LoginPageLocators.LOGOUT_LINK_MODAL), 'Logout modal is not presented'
