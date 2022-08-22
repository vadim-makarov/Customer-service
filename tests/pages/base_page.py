import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class BasePage:
    def __init__(self, browser, url, timeout=0):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_some_page(self, locator: tuple):
        link = self.browser.find_element(locator)
        link.click()

    def is_element_present(self, *args):
        try:
            self.browser.find_element(*args)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_link(self, locator: tuple):
        assert self.is_element_present(locator), f"{locator} is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # def go_to_basket(self):
    #     self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    # def should_be_authorized_user(self):
    #     assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
    #                                                                  " probably unauthorised user"
