"""содержит тесты главной страницы"""
import allure
import pytest

from app.models import User, Service
from tests.ui_tests.pages.locators import MainPageLocators, ReviewPageLocators, ServicePageLocators
from tests.ui_tests.pages.main_page import MainPage
from tests.ui_tests.src.data import PagesData


class TestMainPage:
    """Тесты основной функциональности"""

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Guest can go to all the links")
    @pytest.mark.parametrize('page, locator', PagesData.pages_list, ids=PagesData.endpoints)
    def test_guest_can_go_to_all_the_links(self, main_page: MainPage, page: str, locator: tuple):
        """Проверяет работоспособность всех страниц, доступных на главной странице """

        main_page.find_and_click_element(locator)
        assert page in main_page.driver.current_url, f"Ссылка {page} не активна"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Guest can pass the registration")
    def test_user_can_register(self, main_page: MainPage, user: User):
        """Проверяет возможность регистрации пользователя"""

        main_page.register_user(user)
        success_text = main_page.get_text(MainPageLocators.SUCCESS_REGISTER_ALERT)
        assert user.username in success_text, 'Пользователь не смог зарегистроваться'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("User can leave a review")
    def test_user_can_leave_a_review(self, main_page: MainPage, user: User):
        """Пользователь может оставить отзыв"""
        main_page.register_user(user) \
            .find_and_click_element(MainPageLocators.REVIEWS_PAGE_LINK) \
            .leave_a_review(user)
        message = main_page.get_text(ReviewPageLocators.THANK_YOU_MESSAGE)
        assert 'Thank you' in message, "Сообщение об успешной отправке отзыва не получено"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("User can add a service")
    def test_user_can_add_a_service(self, main_page: MainPage, user: User, new_service: Service):
        """User can add a service"""
        main_page.register_user(user) \
            .select_service_and_continue(new_service) \
            .is_element_present(ServicePageLocators.SERVICE_ALERT, "Запись создана") \
            .change_service() \
            .is_element_present(ServicePageLocators.SERVICE_ALERT, "Запись не изменена") \
            .delete_service()
        message = main_page.get_text(ServicePageLocators.SERVICE_ALERT)
        assert 'Item deleted.' in message, "Сообщение об удалении записи не получено"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("User can change his data")
    def test_user_can_edit_profile(self, main_page: MainPage, user: User):
        """User can change his own profile"""
        main_page.register_user(user) \
            .find_and_click_element(MainPageLocators.USER_BUTTON) \
            .find_and_click_element(ServicePageLocators.EDIT_PROFILE_BUTTON) \
            .find_element_and_input_data(ServicePageLocators.EDIT_PHONE_NUM_FIELD, '') \
            .find_and_click_element(ServicePageLocators.SUBMIT_CHANGE_USER_DATA_BUTTON) \
            .confirm_sms_code()
        message = main_page.get_text(ServicePageLocators.SERVICE_ALERT)
        assert 'Values has been changed' in message, "Пользовательские данные не изменены"
