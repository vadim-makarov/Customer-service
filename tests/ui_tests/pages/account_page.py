"""Contains account test class"""
from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.src.models import TestService


class AccountPage(BasePage):
    """Contains account page methods"""

    SERVICE_1 = (By.CSS_SELECTOR, "#service1")
    SERVICE_2 = (By.CSS_SELECTOR, "#service2")
    SERVICE_3 = (By.CSS_SELECTOR, "#service3")
    MODAL_SERVICE_2 = (By.CSS_SELECTOR, "div[class^='modal-body'] > div > form > div > select[id='service2']")
    SERVICE_DATE = (By.CSS_SELECTOR, "#service_date")
    SERVICE_TIME = (By.CSS_SELECTOR, "#service_time")
    CONFIRM_SERVICE_BUTTON = (By.CSS_SELECTOR, "form > div > input[type='submit']")
    CONFIRM_CHANGE_SERVICE_MODAL_BUTTON = (By.CSS_SELECTOR, "div > div > input[id='submit']")
    SERVICE_ALERT = (By.CSS_SELECTOR, "div[class^='alert']")
    DOWN_ANCHOR = (By.CSS_SELECTOR, "span[class^='mb-3']")
    EDIT_SERVICE_BUTTON = (By.CSS_SELECTOR, "button[data-bs-target*='#editModal']")
    CHANGE_SERVICE_SUBMIT_BUTTON = (By.CSS_SELECTOR, "div[class='modal-footer'] > div > input")
    DELETE_SERVICE_BUTTON = (By.CSS_SELECTOR, "button[data-bs-target*='#deleteModal']")
    CONFIRM_DELETE_SERVICE_BUTTON = (By.CSS_SELECTOR, "form > input[class$='danger']")
    EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, "button[data-bs-target*='#profileModal']")
    EDIT_PHONE_NUM_FIELD = (By.CSS_SELECTOR, "form > div > input[type='tel']")
    SUBMIT_CHANGE_USER_DATA_BUTTON = (By.CSS_SELECTOR, "p > input[type='submit']")

    def select_service_and_continue(self, new_service: TestService) -> AccountPage:
        """Заполняет поля и добавляет сервис"""
        self.find_and_click_element(self.USER_BUTTON) \
            .select_value(self.SERVICE_1, new_service.service1) \
            .select_value(self.SERVICE_2, new_service.service2) \
            .select_value(self.SERVICE_3, new_service.service3) \
            .find_element_and_input_data(self.SERVICE_DATE, new_service.service_date) \
            .select_value(self.SERVICE_TIME, new_service.service_time) \
            .find_and_click_element(self.CONFIRM_SERVICE_BUTTON)
        return self

    def change_service(self) -> AccountPage:
        """Изменяет существующий сервис"""
        self.find_and_click_element(self.EDIT_SERVICE_BUTTON)
        self.wait.until(EC.element_to_be_clickable(self.MODAL_SERVICE_2))
        self.select_value(self.MODAL_SERVICE_2, 'Fanta') \
            .find_and_click_element(self.CHANGE_SERVICE_SUBMIT_BUTTON)
        return self

    def delete_service(self) -> AccountPage:
        """Удаляет существующий сервис"""
        self.find_and_click_element(self.DELETE_SERVICE_BUTTON) \
            .find_and_click_element(self.CONFIRM_DELETE_SERVICE_BUTTON)
        return self

    def change_profile_data(self, data: str):
        """Changes user's data with edit profile modal"""
        self.find_and_click_element(self.EDIT_PROFILE_BUTTON) \
            .find_element_and_input_data(self.EDIT_PHONE_NUM_FIELD, data) \
            .find_and_click_element(self.SUBMIT_CHANGE_USER_DATA_BUTTON)
        from tests.ui_tests.pages.sms_page import SMSPage
        return SMSPage(self.driver)
