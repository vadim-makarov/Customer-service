from tests.ui_tests.pages.locators import ReviewPageLocators
from tests.ui_tests.pages.register_page import RegisterPage


class ReviewPage(RegisterPage):

    def review_page_is_empty(self):
        assert not self.is_element_present(*ReviewPageLocators.EXIST_REVIEW), 'There is a review on the page'

    def guest_cant_leave_a_review(self):
        assert not self.is_element_present(*ReviewPageLocators.MODAL_REVIEW_BUTTON), 'Review button is present'

    def user_should_see_a_leave_review_button(self):
        assert self.is_element_present(*ReviewPageLocators.MODAL_REVIEW_BUTTON), 'Review button is not present'

    def user_can_leave_a_review(self):
        self.browser.find_element(*ReviewPageLocators.MODAL_REVIEW_BUTTON).click()
        self.browser.find_element(*ReviewPageLocators.SEND_REVIEW_RATING).click()
        self.browser.find_element(*ReviewPageLocators.SEND_REVIEW_TEXT).send_keys('Some random text')
        self.browser.find_element(*ReviewPageLocators.SEND_REVIEW_BUTTON).click()

    def thank_you_review_message(self):
        message = self.browser.find_element(*ReviewPageLocators.THANK_YOU_MESSAGE).text
        assert 'Thank you' in message, "You don't send a review"
