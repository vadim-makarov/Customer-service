"""Содержит класс главной страницы"""

from selenium.webdriver.remote.webdriver import WebDriver

from app.models import User
from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.locators import MainPageLocators, RegisterPageLocators
from tests.ui_tests.src.data import URLs


class MainPage(BasePage):
    """Cодержит методы взаимодействия с главной страницей и её элементами"""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url = URLs.main_page_url

    def register_user(self, user: User):
        """Регистрирует нового пользователя и вводит смс код"""
        self.find_and_click_element(MainPageLocators.REGISTER_LINK) \
            .find_element_and_input_data(RegisterPageLocators.REGISTER_FORM_NAME, user.username) \
            .find_element_and_input_data(RegisterPageLocators.REGISTER_FORM_PHONE_NUMBER, user.phone_number) \
            .find_and_click_element(RegisterPageLocators.REGISTER_FORM_SEND_SMS)
        sms_code = self.get_text(RegisterPageLocators.SMS_ALERT_CODE).split()[-1]
        self.find_element_and_input_data(RegisterPageLocators.SMS_CODE_FORM, sms_code)
        self.find_and_click_element(RegisterPageLocators.SMS_CONFIRM)
