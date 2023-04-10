import pytest

from app.models import User
from tests.ui_tests.pages.locators import MainPageLocators
from tests.ui_tests.pages.main_page import MainPage
from tests.ui_tests.src.data import PagesData


class TestMainPage:

    @pytest.mark.smoke
    @pytest.mark.parametrize('page, locator', PagesData.pages_list, ids=PagesData.endpoints)
    def test_guest_should_see_some_link(self, main_page: MainPage, page: str, locator: tuple):
        """Проверяет работоспособность всех страниц, доступных на главной странице """
        main_page.find_and_click_element(locator)
        assert main_page.should_be_some_page(page)

    def test_user_can_register(self, main_page: MainPage, user: User):
        """Проверяет возможность регистрации пользователя"""

        main_page.register_user(user)
        success_text = main_page.get_text(MainPageLocators.SUCCESS_REGISTER_ALERT)
        assert user.username in success_text, 'Пользователь не смог зарегистроваться'
