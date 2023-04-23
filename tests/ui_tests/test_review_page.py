"""Contains class for testing review page"""
import allure
from selenium.webdriver.remote.webdriver import WebDriver

from app.models import User
from tests.ui_tests.pages.locators import ReviewPageLocators, MainPageLocators
from tests.ui_tests.pages.main_page import MainPage
from tests.ui_tests.pages.review_page import ReviewPage


class TestReviewPage:
    """Contains review page tests"""

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("User can leave a review")
    def test_user_can_leave_a_review(self, main_page: MainPage, user: User, driver: WebDriver):
        """User can leave a review"""
        main_page.register_user(user) \
            .find_and_click_element(MainPageLocators.REVIEWS_PAGE_LINK)
        review_page = ReviewPage(driver)
        review_page.leave_a_review(user)
        message = review_page.get_text(ReviewPageLocators.THANK_YOU_MESSAGE)
        assert 'Thank you' in message, "Сообщение об успешной отправке отзыва не получено"
