import pytest

from tests.pages.base_page import BasePage
from tests.pages.locators import MainPageLocators
from tests.pages.main_page import MainPage


class TestMainPage:
    LINK = "http://localhost:5000/main/index"

    PAGES_LOCATORS: list[tuple[str, str]] = [MainPageLocators.MAIN_PAGE_LINK,
                                             MainPageLocators.FEATURES_PAGE_LINK,
                                             MainPageLocators.PRICING_PAGE_LINK,
                                             MainPageLocators.REVIEWS_PAGE_LINK,
                                             MainPageLocators.LOGIN_LINK,
                                             MainPageLocators.REGISTER_LINK]

    PAGES = ['index', 'features', 'pricing', 'reviews', 'login', 'register']

    @pytest.mark.parametrize('word', PAGES)
    def test_page_response(self, app_test_client, word: str):
        request = app_test_client.get(self.LINK)
        assert request.status_code == 200
        assert word in request.text

    @pytest.mark.parametrize('locator', PAGES_LOCATORS)
    def test_guest_should_see_some_link(self, browser, locator: tuple):
        page = MainPage(browser, self.LINK)
        page.open()
        page.should_be_element(locator)

    @pytest.mark.parametrize('page_name, link', list(zip(PAGES, PAGES_LOCATORS)))
    def test_guest_can_go_to_link_page(self, browser, page_name: str, link: tuple):
        page = MainPage(browser, self.LINK)
        page.open()
        page.go_to_some_page(link)
        test_page = BasePage(browser, browser.current_url)
        test_page.should_be_some_page(page_name)
