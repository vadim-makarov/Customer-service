"""Contains register page class"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.sms_page import SMSPage
from tests.ui_tests.src.models import TestUser


class RegisterPage(BasePage):
    """Contains methods and locators of the register page"""

    REGISTER_FORM_NAME = (By.ID, 'username')
    REGISTER_FORM_PHONE_NUMBER = (By.ID, 'phone_number')
    SUBMIT_BUTTON = (By.ID, 'confirm')

    def fill_user_data_and_continue(self, user: TestUser):
        """Регистрирует нового пользователя и вводит смс код"""
        self.wait.until(EC.url_contains('register'), "Register page in not opened")
        self.find_element_and_input_data(self.REGISTER_FORM_NAME, user.username) \
            .find_element_and_input_data(self.REGISTER_FORM_PHONE_NUMBER, user.phone_number) \
            .find_and_click_element(self.SUBMIT_BUTTON)
        return SMSPage(self.driver)
