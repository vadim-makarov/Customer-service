"""Contains main page class"""
from tests.ui_tests.pages.base_page import BasePage


class MainPage(BasePage):
    """Contains main page methods and locators"""

    def go_to_register_page(self):
        self.find_and_click_element(self.REGISTER_LINK)
        from tests.ui_tests.pages.auth_page import AuthPage
        return AuthPage(self.driver)

    def go_to_review_page(self):
        self.find_and_click_element(self.REVIEWS_PAGE_LINK)
        from tests.ui_tests.pages.review_page import ReviewPage
        return ReviewPage(self.driver)

    def go_to_account_page(self):
        self.find_and_click_element(self.USER_BUTTON)
        from tests.ui_tests.pages.account_page import AccountPage
        return AccountPage(self.driver)
