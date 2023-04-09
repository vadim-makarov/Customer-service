import pytest

from tests.ui_tests.pages.main_page import MainPage
from tests.ui_tests.src.data import PagesData


class TestMainPage:

    @pytest.mark.smoke
    @pytest.mark.parametrize('page, locator', PagesData.pages_list)
    def test_guest_should_see_some_link(self, main_page: MainPage, page: str, locator: tuple):
        """Проверяет работоспособность всех страниц, доступных на главной странице """
        main_page.find_and_click_element(locator)
        assert main_page.should_be_some_page(page)
