"""Содержит класс страницы регистрации"""
import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.register_page import RegisterPage


class TestRegisterPage:
    """Содержит методы страницы регистрации"""
    def test_should_be_login_page(self, driver):
        page = LoginPage(driver, self.LOGIN_LINK)
        page.open()
        page.should_be_login_page()

    def test_should_be_registration_link(self, driver):
        page = LoginPage(driver, self.LOGIN_LINK)
        page.open()
        page.can_go_register_from_login()

    def test_should_be_registration_page(self, driver):
        page = RegisterPage(driver, self.REGISTER_LINK)
        page.open()
        page.should_be_register_page()

    def test_guest_is_not_logged_in(self, driver):
        page = LoginPage(driver, self.LOGIN_LINK)
        page.open()
        page.guest_should_not_be_logged_in()

    def test_sms_resend_button_is_not_active(self, driver, user):
        page = RegisterPage(driver, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.user_cant_resend_sms_in_minute()

    @pytest.mark.skip(reason="slow")
    @pytest.mark.slow
    def test_sms_resend_button_is_active(self, driver, user):
        page = RegisterPage(driver, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.user_can_resend_sms_in_minute()

    def test_registration_positive(self, driver, user):
        page = RegisterPage(driver, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.send_sms_code()
        page.user_is_registered()
        page.log_out_user()

    def test_user_is_logged_in(self, driver, user):
        page = RegisterPage(driver, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.send_sms_code()
        page = LoginPage(driver, self.LOGIN_LINK)
        page.user_should_be_logged_in()
        page.log_out_user()

    def test_user_can_log_out(self, driver, user):
        page = RegisterPage(driver, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.send_sms_code()
        page = LoginPage(driver, self.LOGIN_LINK)
        page.user_should_be_logged_in()
        page.log_out_user()
        page.guest_should_not_be_logged_in()

    def test_user_is_already_registered(self, driver, user):
        page = RegisterPage(driver, self.REGISTER_LINK)
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.send_sms_code()
        page.log_out_user()
        page.open()
        page.register_new_user(user.username, user.phone_number)
        page.should_not_be_sms_page()
