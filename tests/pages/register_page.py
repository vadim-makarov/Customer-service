from base_page import BasePage
from locators import RegisterPageLocators


class RegisterPage(BasePage):
    def should_be_register_page(self):
        self.should_be_register_url()
        self.should_be_register_form_name()
        self.should_be_register_form_phone()
        self.should_be_register_link()

    def should_be_register_url(self):
        assert 'register' in self.browser.current_url, 'This is not a Register page'

    def should_be_register_form_name(self):
        assert self.browser.find_element(*RegisterPageLocators.REGISTER_FORM_NAME), 'Register form_name is not presented'

    def should_be_register_form_phone(self):
        assert self.browser.find_element(
            *RegisterPageLocators.REGISTER_FORM_PHONE_NUMBER), 'Register form_phone is not presented'

    def should_be_register_link(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_TO_REG_PAGE), 'Reg link is not presented'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FORM)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FORM)
        password_field.send_keys(password)
        submit_password = self.browser.find_element(*LoginPageLocators.SUBMIT_PASSWORD)
        submit_password.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()