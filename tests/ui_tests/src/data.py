"""Модуль содержит класс с url """

from tests.ui_tests.pages.locators import MainPageLocators


class URLs:
    """Класс содержит локальные url-ы"""
    main_page_url = 'http://localhost:5000/'
    login_page_url = 'http://localhost:5000/auth/login'
    register_page_url = 'http://localhost:5000/auth/register'
    account_page_url = 'http://localhost:5000/user/'
    review_page_url = 'http://localhost:5000/reviews'


class PagesData:
    """Содержит локаторы главной страницы и эндпоинты """
    main_page_links_locators: list[tuple[str, str]] = [MainPageLocators.MAIN_PAGE_LINK,
                                                       MainPageLocators.FEATURES_PAGE_LINK,
                                                       MainPageLocators.PRICING_PAGE_LINK,
                                                       MainPageLocators.REVIEWS_PAGE_LINK,
                                                       MainPageLocators.LOGIN_LINK,
                                                       MainPageLocators.REGISTER_LINK]

    endpoints: list[str] = ['index', 'features', 'pricing', 'reviews', 'login', 'register']

    pages_list: list[tuple[list, list]] = list(zip(endpoints, main_page_links_locators))
