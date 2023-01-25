from tests.ui_tests.pages.register_page import RegisterPage
from tests.ui_tests.pages.review_page import ReviewPage


class TestReviewPage:
    REVIEW_LINK = 'http://localhost:5000/reviews'

    def test_guest_cant_leave_review(self, browser):
        page = ReviewPage(browser, self.REVIEW_LINK)
        page.open()
        page.review_page_is_empty()
        page.guest_cant_leave_a_review()

    def test_user_can_leave_a_review(self, browser, user):
        reg = RegisterPage(browser, 'http://localhost:5000/auth/register')
        reg.open()
        reg.register_new_user(user.username, user.phone_number)
        reg.send_sms_code()
        page = ReviewPage(browser, self.REVIEW_LINK)
        page.open()
        page.user_should_see_a_leave_review_button()
        page.user_can_leave_a_review()
        page.thank_you_review_message()
