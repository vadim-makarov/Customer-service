from selenium.common.exceptions import NoSuchElementException

from tests.pages.locators import LoginPageLocators


class BasePage:

    def __init__(self, browser, url: str, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_element(self, locator: tuple):
        assert self.is_element_present(*locator), f"{locator} is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_active(self, how, what):
        return self.browser.find_element(how, what).is_enabled()

    def should_be_some_page(self, page_name: str):
        assert page_name in self.browser.current_url, f'This is not a {page_name} page'

    def go_to_some_page(self, locator: tuple):
        link = self.browser.find_element(*locator)
        link.click()

    def log_out_user(self):
        self.browser.find_element(*LoginPageLocators.LOGOUT_LINK).click()
        self.browser.find_element(*LoginPageLocators.LOGOUT_LINK_MODAL).click()
