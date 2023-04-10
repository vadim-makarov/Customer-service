import allure
import pytest

from app.models import User
from tests.ui_tests.pages.locators import MainPageLocators, ReviewPageLocators
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
        assert main_page.should_be_some_page(page)

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

    @pytest.mark.skip(reason='Not implemented yet')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("User can add a service")
    def test_user_can_add_a_service(self, main_page: MainPage, user: User):
        """User can add a service"""
        main_page.register_user(user) \
            .find_and_click_element()
