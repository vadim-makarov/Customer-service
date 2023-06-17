"""Contains a review page class"""
from __future__ import annotations

from random import randint

from selenium.webdriver.common.by import By

from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.src.models import TestReview


class ReviewPage(BasePage):
    """Contains a review page methods"""

    MODAL_REVIEW_BUTTON = (By.CSS_SELECTOR, 'body > main > main > div.vstack.gap-2.col-md-5.mx-auto > button')
    REVIEW_RATING_RADIO_BUTTON = (By.CSS_SELECTOR, f'#rating-{randint(0, 4)}')
    SEND_REVIEW_TEXT = (By.CSS_SELECTOR, '#text')
    SEND_REVIEW_BUTTON = (By.CSS_SELECTOR, '#send_review')
    EXIST_REVIEW = (By.CSS_SELECTOR, 'body > main > main > div.container > div > div > div')
    THANK_YOU_MESSAGE = (By.XPATH, '/html/body/div')

    def leave_a_review(self, review: TestReview) -> ReviewPage:
        """Writes and sends a review"""
        self.find_and_click_element(self.MODAL_REVIEW_BUTTON) \
            .find_and_click_element(self.REVIEW_RATING_RADIO_BUTTON) \
            .find_element_and_input_data(self.SEND_REVIEW_TEXT, review.text) \
            .find_and_click_element(self.SEND_REVIEW_BUTTON)
        return self
