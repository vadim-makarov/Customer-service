"""Contains account page test class"""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from app.models import User
from tests.ui_tests.pages.account_page import AccountPage
from tests.ui_tests.pages.locators import AccountPageLocators
from tests.ui_tests.pages.main_page import MainPage
from tests.ui_tests.src.models import TestService


class TestAccountPage:
    """Contains account page tests"""

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("User can add a service")
    def test_user_can_add_a_service(self, main_page: MainPage, user: User, new_service: TestService, driver: WebDriver):
        """User can add a service"""
        main_page.fill_user_data_and_continue(user)
        account_page = AccountPage(driver)
        account_page.select_service_and_continue(new_service) \
            .is_element_present(AccountPageLocators.SERVICE_ALERT, "Запись создана") \
            .change_service() \
            .is_element_present(AccountPageLocators.SERVICE_ALERT, "Запись не изменена") \
            .delete_service()
        message = account_page.get_text(AccountPageLocators.SERVICE_ALERT)
        assert 'Item deleted.' in message, "Сообщение об удалении записи не получено"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("User can change his data")
    def test_user_can_edit_profile(self, main_page: MainPage, user: User, driver: WebDriver):
        """User can change his own profile"""
        main_page.fill_user_data_and_continue(user) \
            .find_and_click_element(MainPageLocators.USER_BUTTON)
        account_page = AccountPage(driver)
        phone_number = generate_phone_number()
        account_page.change_profile_data(phone_number)
        message = main_page.get_text(AccountPageLocators.SERVICE_ALERT)
        assert 'Values has been changed' in message, "Пользовательские данные не изменены"
