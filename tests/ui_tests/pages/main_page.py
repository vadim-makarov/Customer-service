"""Contains main page class"""
from tests.ui_tests.pages.auth_page import AuthPage
from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.review_page import ReviewPage


class MainPage(BasePage):
    """Contains main page methods and locators"""

    def go_to_register_page(self):
        self.find_and_click_element(self.REGISTER_LINK)
        return AuthPage(self.driver)

    def go_to_review_page(self):
        self.find_and_click_element(self.REVIEWS_PAGE_LINK)
        return ReviewPage(self.driver)
