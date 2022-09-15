from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.ui_tests.pages.locators import ReviewPageLocators
from tests.ui_tests.pages.register_page import RegisterPage


class ReviewPage(RegisterPage):

    def review_page_is_empty(self):
        assert not self.is_element_present(*ReviewPageLocators.EXIST_REVIEW)

    def guest_cant_leave_a_review(self):
        assert not self.is_element_present(*ReviewPageLocators.MODAL_REVIEW_BUTTON)

    def user_should_see_a_leave_review_button(self):
        assert self.is_element_present(*ReviewPageLocators.MODAL_REVIEW_BUTTON)

    def user_can_leave_a_review(self):
        # review_btn = self.browser.find_element(*ReviewPageLocators.MODAL_REVIEW_BUTTON)
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(ReviewPageLocators.MODAL_REVIEW_BUTTON)).click()
        # self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # _ = review_btn.location_once_scrolled_into_view
        # review_btn.click()
        self.browser.find_element(*ReviewPageLocators.SEND_REVIEW_RATING).click()
        self.browser.find_element(*ReviewPageLocators.SEND_REVIEW_TEXT).send_keys('Some random text')
        self.browser.find_element(*ReviewPageLocators.SEND_REVIEW_BUTTON).click()

    def thank_you_review_message(self):
        message = self.browser.find_element(*ReviewPageLocators.THANK_YOU_MESSAGE).text
        # alert = self.browser.switch_to.alert.text
        # print(message)
        assert 'Thank you' in message, "You don't send a review"
