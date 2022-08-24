from tests.pages.base_page import BasePage
from tests.pages.locators import RegisterPageLocators


class RegisterPage(BasePage):

    REGISTER_LINK = 'http://127.0.0.1:5000/auth/register'
    NAME = 'VadimM'
    PHONE = '+79022513250'

    def should_be_register_page(self):
        self.should_be_some_page(self.REGISTER_LINK)
        self.should_be_register_form_name()
        self.should_be_register_form_phone()

    def should_be_register_form_name(self):
        assert self.browser.find_element(
            *RegisterPageLocators.REGISTER_FORM_NAME), 'Register form_name is not presented'

    def should_be_register_form_phone(self):
        assert self.browser.find_element(
            *RegisterPageLocators.REGISTER_FORM_PHONE_NUMBER), 'Register form_phone is not presented'

    def register_new_user(self, name: str = NAME, phone: str = PHONE):
        self.browser.find_element(*RegisterPageLocators.REGISTER_FORM_NAME).send_keys(name)
        self.browser.find_element(*RegisterPageLocators.REGISTER_FORM_PHONE_NUMBER).send_keys(phone)
        self.browser.find_element(*RegisterPageLocators.REGISTER_FORM_SEND_SMS).click()
        code = self.browser.find_element(*RegisterPageLocators.SMS_ALERT_CODE).text
        code = code.split()[-1]
        self.browser.find_element(*RegisterPageLocators.SMS_CODE_FORM).send_keys(code)
        self.browser.find_element(*RegisterPageLocators.SMS_CONFIRM).click()

    def user_is_registered(self):
        alert = self.browser.find_element(*RegisterPageLocators.SMS_ALERT_CODE).text
        assert self.NAME in alert, 'User is not registered!'
