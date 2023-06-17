"""Contains class for testing review page"""
import allure

from tests.ui_tests.pages.main_page import MainPage
from tests.ui_tests.pages.review_page import ReviewPage
from tests.ui_tests.src.models import TestUser


class TestReviewPage:
    """Contains review page tests"""

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("User can leave a review")
    def test_user_can_leave_a_review(self, main_page: MainPage, user: TestUser, request):
        """User can leave a review"""
        main_page.go_to_register_page() \
            .fill_user_data_and_continue(user) \
            .confirm_sms_code(request) \
            .go_to_review_page() \
            .leave_a_review(user)
        message = main_page.get_text(ReviewPage.THANK_YOU_MESSAGE)
        assert 'Thank you' in message, "Сообщение об успешной отправке отзыва не получено"
