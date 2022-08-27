from pages.base_page import BasePage
from pages.locators import ReviewPageLocators, MainPageLocators
from pages.register_page import RegisterPage


class ReviewPage(BasePage, RegisterPage):
    REVIEW_LINK = 'http://127.0.0.1:5000/main/reviews'

    def review_page_is_empty(self):
        pass

    def guest_cant_leave_a_review(self):
        assert not self.is_element_present(*ReviewPageLocators.LEAVE_REVIEW_MODAL)

    def user_should_see_a_leave_review_button(self):
        assert self.is_element_present(*ReviewPageLocators.LEAVE_REVIEW_MODAL)

    def register_user_and_go_to_review_page(self):
        self.go_to_some_page(MainPageLocators.REGISTER_LINK)
        self.register_new_user()
        self.send_sms_code()
        self.go_to_some_page(MainPageLocators.REVIEWS_PAGE_LINK)


    def user_can_leave_a_review(self):
        pass