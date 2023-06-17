"""Contains SMS page class"""
from selenium.webdriver.common.by import By

from tests.ui_tests.pages.account_page import AccountPage
from tests.ui_tests.pages.base_page import BasePage


class SMSPage(BasePage):
    """Contains SMS page methods and locators"""

    SMS_CODE_FORM = (By.ID, 'code_input')
    SMS_CONFIRM = (By.CSS_SELECTOR, "button[value='Register']")
    SMS_ALERT_CODE = (By.CSS_SELECTOR, 'body > div.alert.alert-info.fade.show')

    def confirm_sms_code(self, request):
        """Inputs a code and pushes 'Confirm' button"""
        sms_code_message = self.get_text(self.SMS_ALERT_CODE)
        sms_code = sms_code_message.split()[-1]
        self.find_element_and_input_data(self.SMS_CODE_FORM, sms_code) \
            .find_and_click_element(self.SMS_CONFIRM)
        if 'edit' in request.node.name:
            return AccountPage(self.driver)
        return BasePage(self.driver)
