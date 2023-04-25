"""Contains account test class"""
from datetime import datetime
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from app.models import Service
from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.locators import MainPageLocators, AccountPageLocators
from tests.ui_tests.src.data import URLs


class AccountPage(BasePage):
    """Contains account page methods"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = URLs.account_page_url

    def select_service_and_continue(self, new_service: Service):
        """Заполняет поля и добавляет сервис"""
        self.find_and_click_element(MainPageLocators.USER_BUTTON) \
            .select_value(AccountPageLocators.SERVICE_1, new_service.service1) \
            .select_value(AccountPageLocators.SERVICE_2, new_service.service2) \
            .select_value(AccountPageLocators.SERVICE_3, new_service.service3) \
            .find_element_and_input_data(AccountPageLocators.SERVICE_DATE,
                                         datetime.strftime(new_service.service_date, "%m-%d-%Y")) \
            .select_value(AccountPageLocators.SERVICE_TIME, new_service.service_time) \
            .find_and_click_element(AccountPageLocators.CONFIRM_SERVICE_BUTTON)
        return self

    def change_service(self):
        """Изменяет существующий сервис"""
        self.find_and_click_element(AccountPageLocators.EDIT_SERVICE_BUTTON)
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.MODAL_SERVICE_2))
        self.select_value(AccountPageLocators.MODAL_SERVICE_2, 'Fanta') \
            .find_and_click_element(AccountPageLocators.CHANGE_SERVICE_SUBMIT_BUTTON)
        return self

    def delete_service(self):
        """Удаляет существующий сервис"""
        self.find_and_click_element(AccountPageLocators.DELETE_SERVICE_BUTTON) \
            .find_and_click_element(AccountPageLocators.CONFIRM_DELETE_SERVICE_BUTTON)

    def change_profile_data(self, data: str):
        """Changes user's data with edit profile modal"""
        self.find_and_click_element(AccountPageLocators.EDIT_PROFILE_BUTTON) \
            .find_element_and_input_data(AccountPageLocators.EDIT_PHONE_NUM_FIELD, data) \
            .find_and_click_element(AccountPageLocators.SUBMIT_CHANGE_USER_DATA_BUTTON) \
            .confirm_sms_code()
