"""Содержит класс главной страницы"""
from selenium.webdriver.remote.webdriver import WebDriver

from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.src.data import URLs


class MainPage(BasePage):
    """содержит методы взаимодействия с главной страницей и её элементами"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = URLs.main_page_url
