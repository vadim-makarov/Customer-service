from pages.review_page import ReviewPage


class TestReviewPage:
    REVIEW_LINK = 'http://127.0.0.1:5000/main/reviews'

    def test_guest_cant_leave_review(self, browser):
        page = ReviewPage(browser, self.REVIEW_LINK)
        page.open()
        page.guest_cant_leave_a_review()

    def test_user_should_see_a_review_send_button(self, browser):
        page = ReviewPage(browser, self.REVIEW_LINK)
        page.open()
        page.register_user_and_go_to_review_page()
        page.user_should_see_a_leave_review_button()

    def test_user_can_leave_a_review(self, browser):
        page = ReviewPage(browser, self.REVIEW_LINK)
        page.open()
        page.register_user_and_go_to_review_page()