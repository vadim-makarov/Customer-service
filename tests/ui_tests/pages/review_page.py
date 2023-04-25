"""Contains a review page class"""
from selenium.webdriver.remote.webdriver import WebDriver

from app.models import User
from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.locators import ReviewPageLocators
from tests.ui_tests.src.data import URLs


class ReviewPage(BasePage):
    """Contains a review page methods"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = URLs.review_page_url

    def leave_a_review(self, user: User):
        """Пишет и отправляет отзыв"""
        self.find_and_click_element(ReviewPageLocators.MODAL_REVIEW_BUTTON) \
            .find_and_click_element(ReviewPageLocators.SEND_REVIEW_RATING) \
            .find_element_and_input_data(ReviewPageLocators.SEND_REVIEW_TEXT, user.fake.paragraph(nb_sentences=5)) \
            .find_and_click_element(ReviewPageLocators.SEND_REVIEW_BUTTON)
        return self
