from tests.pages.locators import ReviewPageLocators
from tests.pages.register_page import RegisterPage


class ReviewPage(RegisterPage):

    def review_page_is_empty(self):
        pass

    def guest_cant_leave_a_review(self):
        assert not self.is_element_present(*ReviewPageLocators.LEAVE_REVIEW_MODAL)

    def user_should_see_a_leave_review_button(self):
        assert self.is_element_present(*ReviewPageLocators.LEAVE_REVIEW_MODAL)


    def user_can_leave_a_review(self):
        pass
