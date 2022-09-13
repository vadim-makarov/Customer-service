import pytest
from flask_login import login_user

from tests.pages.review_page import ReviewPage


class TestReviewPage:
    REVIEW_LINK = 'http://localhost:5000/reviews'

    def test_guest_cant_leave_review(self, browser):
        page = ReviewPage(browser, self.REVIEW_LINK)
        page.open()
        page.guest_cant_leave_a_review()

    @pytest.mark.xfail
    def test_user_should_see_a_review_send_button(self, browser, user):
        login_user(user, force=True)
        page = ReviewPage(browser, self.REVIEW_LINK)
        page.open()
        page.user_should_see_a_leave_review_button()

    @pytest.mark.xfail
    def test_user_can_leave_a_review(self, browser, user):
        login_user(user, force=True)
        page = ReviewPage(browser, self.REVIEW_LINK)
        page.open()
