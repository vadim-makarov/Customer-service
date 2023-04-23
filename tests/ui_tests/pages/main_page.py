"""Содержит класс главной страницы"""
from datetime import datetime

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from app.models import User, Service
from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.locators import MainPageLocators, RegisterPageLocators, ReviewPageLocators, \
    ServicePageLocators
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
            .find_and_click_element(RegisterPageLocators.REGISTER_FORM_SEND_SMS) \
            .confirm_sms_code()
        return self

    def confirm_sms_code(self):
        """Вводит смс код"""
        sms_code = self.get_text(RegisterPageLocators.SMS_ALERT_CODE).split()[-1]
        self.find_element_and_input_data(RegisterPageLocators.SMS_CODE_FORM, sms_code) \
            .find_and_click_element(RegisterPageLocators.SMS_CONFIRM)
        return self

    def leave_a_review(self, user: User):
        """Пишет и отправляет отзыв"""
        self.find_and_click_element(ReviewPageLocators.MODAL_REVIEW_BUTTON) \
            .find_and_click_element(ReviewPageLocators.SEND_REVIEW_RATING) \
            .find_element_and_input_data(ReviewPageLocators.SEND_REVIEW_TEXT, user.fake.paragraph(nb_sentences=5)) \
            .find_and_click_element(ReviewPageLocators.SEND_REVIEW_BUTTON)

    def select_service_and_continue(self, new_service: Service):
        """Заполняет поля и добавляет сервис"""
        self.find_and_click_element(MainPageLocators.USER_BUTTON) \
            .select_value(ServicePageLocators.SERVICE_1, new_service.service1) \
            .select_value(ServicePageLocators.SERVICE_2, new_service.service2) \
            .select_value(ServicePageLocators.SERVICE_3, new_service.service3) \
            .find_element_and_input_data(ServicePageLocators.SERVICE_DATE,
                                         datetime.strftime(new_service.service_date, "%d%m%Y")) \
            .select_value(ServicePageLocators.SERVICE_TIME, new_service.service_time) \
            .find_and_click_element(ServicePageLocators.CONFIRM_SERVICE_BUTTON)
        return self

    def change_service(self):
        """Изменяет существующий сервис"""
        self.find_and_click_element(ServicePageLocators.EDIT_SERVICE_BUTTON)
        self.wait.until(EC.element_to_be_clickable(ServicePageLocators.MODAL_SERVICE_2))
        self.select_value(ServicePageLocators.MODAL_SERVICE_2, 'Fanta') \
            .find_and_click_element(ServicePageLocators.CHANGE_SERVICE_SUBMIT_BUTTON)
        return self

    def delete_service(self):
        """Удаляет существующий сервис"""
        self.find_and_click_element(ServicePageLocators.DELETE_SERVICE_BUTTON) \
            .find_and_click_element(ServicePageLocators.CONFIRM_DELETE_SERVICE_BUTTON)
