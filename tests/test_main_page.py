import pytest

from tests.pages.locators import MainPageLocators
from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage

LOGIN_LINK = 'http://127.0.0.1:5000/auth/login'
HOME_LINK = "http://127.0.0.1:5000/main/index"


class TestLoginFromMainPage:
    page_links = [MainPageLocators.MAIN_PAGE_LINK,
                  MainPageLocators.FEATURES_PAGE_LINK,
                  MainPageLocators.PRICING_PAGE_LINK,
                  MainPageLocators.PRICING_PAGE_LINK,
                  MainPageLocators.LOGIN_LINK,
                  MainPageLocators.REGISTER_LINK]
    pages = ['index', 'features', 'pricing', 'reviews', 'login', 'register']

    @pytest.mark.parametrize('link', page_links)
    def test_guest_should_see_some_link(self, browser, link):
        page = MainPage(browser, HOME_LINK)
        page.open()
        page.should_be_link(link)

    @pytest.mark.parametrize('page, link', list(zip(pages, page_links)))
    def test_guest_can_go_to_link_page(self, browser, page, link: tuple):
        page = MainPage(browser, HOME_LINK)
        page.open()
        page.go_to_some_page(link)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_page()
