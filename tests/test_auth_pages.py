from itertools import product

import pytest

from tests.pages.login_page import LoginPage
from tests.pages.register_page import RegisterPage


class TestRegisterPage:
    LOGIN_LINK = 'http://127.0.0.1:5000/auth/login'
    REGISTER_LINK = 'http://127.0.0.1:5000/auth/register'

    INVALID_NAMES = ['', '<script>alert(123)</script>', '^$^&&#',
                     'DS', '     ', 'JS    ', '    J_S']

    INVALID_PHONES = ['<script>alert(123)</script>', '+53252253f3252',
                      '', '           ',
                      '+78987566    ', '+6787654354329', '+77777777777']

    COMBINATIONS = product(INVALID_NAMES, INVALID_PHONES)

    def test_should_be_login_page(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.should_be_login_page()

    def test_should_be_registration_link(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.can_go_register_from_login()

    def test_should_be_registration_page(self, browser):
        page = RegisterPage(browser, self.REGISTER_LINK)
        page.open()
        page.should_be_register_page()

    def test_guest_is_not_logged_in(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.guest_should_not_be_logged_in()

    def test_sms_resend_button_is_not_active(self, browser, user):
        page = RegisterPage(browser, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.user_cant_resend_sms_in_minute()

    @pytest.mark.skip(reason="slow")
    @pytest.mark.slow
    def test_sms_resend_button_is_active(self, browser, user):
        page = RegisterPage(browser, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.user_can_resend_sms_in_minute()

    def test_registration_positive(self, browser, user):
        page = RegisterPage(browser, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.send_sms_code()
        page.user_is_registered()
        page.log_out_user()

    def test_user_is_logged_in(self, browser, user):
        page = RegisterPage(browser, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.send_sms_code()
        page = LoginPage(browser, self.LOGIN_LINK)
        page.user_should_be_logged_in()
        page.log_out_user()

    def test_user_can_log_out(self, browser, user):
        page = RegisterPage(browser, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.send_sms_code()
        page = LoginPage(browser, self.LOGIN_LINK)
        page.user_should_be_logged_in()
        page.log_out_user()
        page.guest_should_not_be_logged_in()

    @pytest.mark.parametrize('name, phone', COMBINATIONS)
    def test_registration_negative(self, browser, name: str, phone: str):
        page = RegisterPage(browser, self.REGISTER_LINK)
        page.open()
        page.register_new_user(name=name, phone=phone)
        page.should_not_be_sms_page()

    @pytest.mark.xfail(reason='you have to do something with that shit')
    def test_user_is_already_registered(self, browser, user):
        page = RegisterPage(browser, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.should_not_be_sms_page()
