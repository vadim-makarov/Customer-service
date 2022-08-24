from selenium.common.exceptions import NoSuchElementException


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

    def should_be_some_page(self, page_name: str):
        assert page_name in self.browser.current_url, f'This is not a {page_name} page'

    def go_to_some_page(self, locator: tuple):
        link = self.browser.find_element(*locator)
        link.click()

    # def solve_quiz_and_get_code(self):
    #     alert = self.browser.switch_to.alert
    #     x = alert.text.split(" ")[2]
    #     answer = str(math.log(abs((12 * math.sin(float(x))))))
    #     print(answer)
    #     alert.send_keys(answer)
    #     alert.accept()
    #     try:
    #         alert = self.browser.switch_to.alert
    #         alert_text = alert.text
    #         print(f"Your code: {alert_text}")
    #         alert.accept()
    #     except NoAlertPresentException:
    #         print("No second alert presented")

    # def go_to_basket(self):
    #     self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    # def should_be_authorized_user(self):
    #     assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
    #                                                                  " probably unauthorised user"
