from tests.pages.login_page import LoginPage
from tests.pages.register_page import RegisterPage


class TestRegisterPage:
    LOGIN_LINK = 'http://127.0.0.1:5000/auth/login'
    REGISTER_LINK = 'http://127.0.0.1:5000/auth/register'

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
        page.guest_should_not_be_log_on()

    def test_registration(self, browser):
        page = RegisterPage(browser, self.REGISTER_LINK)
        page.open()
        page.register_new_user()
        page.user_is_registered()

    def test_user_is_logged_in(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.user_should_be_log_on()
        page.user_can_log_out()

    def test_user_can_log_out(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.login_user()
        page.user_can_see_logout_link()
        page.user_can_log_out()
        page.guest_should_not_be_log_on()
