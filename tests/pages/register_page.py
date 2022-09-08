import time

from tests.pages.base_page import BasePage
from tests.pages.locators import RegisterPageLocators


class RegisterPage(BasePage):
    REGISTER_LINK = 'http://127.0.0.1:5000/auth/register'

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

    def register_new_user(self, name: str, phone: str):
        self.browser.find_element(*RegisterPageLocators.REGISTER_FORM_NAME).send_keys(name)
        self.browser.find_element(*RegisterPageLocators.REGISTER_FORM_PHONE_NUMBER).send_keys(phone)
        self.browser.find_element(*RegisterPageLocators.REGISTER_FORM_SEND_SMS).click()

    def user_cant_resend_sms_in_minute(self):
        assert self.is_element_active(*RegisterPageLocators.SMS_RESEND), 'Resend SMS button is active.'

    def user_can_resend_sms_in_minute(self):
        code = self.browser.find_element(*RegisterPageLocators.SMS_ALERT_CODE).text
        code = code.split()[-1]
        print('THIS IS A SLOW TEST PLEASE WAIT FOR A MINUTE!')
        time.sleep(61)
        self.is_element_active(*RegisterPageLocators.SMS_RESEND)
        self.browser.find_element(*RegisterPageLocators.SMS_RESEND).click()
        resented_code = self.browser.find_element(*RegisterPageLocators.SMS_ALERT_CODE).text
        resented_code = resented_code.split()[-1]
        assert resented_code != code, "Codes are equal. Seems that resend method doesn't work"

    def should_not_be_sms_page(self):
        self.should_be_some_page('register'), 'This combination should not be valid'

    def send_sms_code(self):
        code = self.browser.find_element(*RegisterPageLocators.SMS_ALERT_CODE).text
        code = code.split()[-1]
        self.browser.find_element(*RegisterPageLocators.SMS_CODE_FORM).send_keys(code)
        self.browser.find_element(*RegisterPageLocators.SMS_CONFIRM).click()

    def user_is_registered(self):
        alert = self.browser.find_element(*RegisterPageLocators.SMS_ALERT_CODE).text
        assert alert, 'User is not registered!'
