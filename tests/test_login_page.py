from tests.pages.login_page import LoginPage


class TestLoginPage:
    LOGIN_LINK = 'http://127.0.0.1:5000/auth/login'

    def test_should_be_login_page(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.should_be_login_page()

    def test_should_be_login_form(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.should_be_login_form_name()

    def test_should_be_registration_link(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.should_be_register_link()

    def test_guest_cant_go_to_service_page(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.guest_should_not_be_log_on()

    def test_user_can_go_to_service_page(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.login_user()
        page.user_should_be_log_on()
        page.user_can_log_out()

    def test_user_can_log_out(self, browser):
        page = LoginPage(browser, self.LOGIN_LINK)
        page.open()
        page.login_user()
        page.user_can_see_logout_link()
        page.user_can_log_out()
        page.guest_should_not_be_log_on()
