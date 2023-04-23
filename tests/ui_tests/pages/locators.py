"""Содержит локаторы. Общий для всех страниц"""
from random import randint

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Содержит локаторы главной страницы"""
    MAIN_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > a')
    FEATURES_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > ul > li:nth-child(1) > a')
    PRICING_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > ul > li:nth-child(2) > a')
    REVIEWS_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > ul > li:nth-child(3) > a')
    LOGIN_LINK = (By.CSS_SELECTOR, ".btn-outline-light")
    REGISTER_LINK = (By.CSS_SELECTOR, 'a.btn:nth-child(2)')
    SUCCESS_REGISTER_ALERT = (By.CSS_SELECTOR, "div[role='alert']")
    USER_BUTTON = (By.CSS_SELECTOR, "div[class='text-end'] > a")


class RegisterPageLocators:
    """Содержит локаторы страницы регистрации"""
    REGISTER_FORM_NAME = (By.CSS_SELECTOR, '#username')
    REGISTER_FORM_PHONE_NUMBER = (By.CSS_SELECTOR, '#phone_number')
    REGISTER_FORM_SEND_SMS = (By.ID, 'confirm')
    SMS_CODE_FORM = (By.ID, 'code_input')
    SMS_CONFIRM = (By.CSS_SELECTOR,
                   'body > main > main > div > div > div > form > div > div.d-grid.gap-2.col-6.mx-auto > div > button.btn.btn-warning')
    SMS_RESEND = (
        By.CSS_SELECTOR, 'body > main > main > div > div > div > form > div > div.d-grid.gap-2.col-6.mx-auto > div')
    SMS_ALERT_CODE = (By.CSS_SELECTOR, 'body > div.alert.alert-info.fade.show')


class LoginPageLocators:
    """Содержит локаторы страницы логина"""
    LOGIN_FORM_NAME = (By.ID, 'username')
    LOGIN_FORM_PHONE_NUMBER = (By.ID, 'phone_number')
    LOGIN_FORM_SUBMIT = (By.ID, 'submit')
    LOGIN_FORM_TO_REG_PAGE = (By.CSS_SELECTOR, 'body > main > main > div > div > div > div > a')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'body > header > div > div > div > button')
    LOGOUT_LINK_MODAL = (By.CSS_SELECTOR, '#logoutModal > div > div > div.modal-footer > a')


class ReviewPageLocators:
    """Содержит локаторы страницы отзывов"""
    MODAL_REVIEW_BUTTON = (By.CSS_SELECTOR, 'body > main > main > div.vstack.gap-2.col-md-5.mx-auto > button')
    SEND_REVIEW_RATING = (By.CSS_SELECTOR, f'#rating-{randint(0, 4)}')
    SEND_REVIEW_TEXT = (By.CSS_SELECTOR, '#text')
    SEND_REVIEW_BUTTON = (By.CSS_SELECTOR, '#send_review')
    EXIST_REVIEW = (By.CSS_SELECTOR, 'body > main > main > div.container > div > div > div')
    THANK_YOU_MESSAGE = (By.XPATH, '/html/body/div')


class ServicePageLocators:
    """Contains locators from the Service page"""
    SERVICE_1 = (By.CSS_SELECTOR, "#service1")
    SERVICE_2 = (By.CSS_SELECTOR, "#service2")
    SERVICE_3 = (By.CSS_SELECTOR, "#service3")
    MODAL_SERVICE_2 = (By.CSS_SELECTOR, "div[class^='modal-body'] > div > form > div > select[id='service2']")
    SERVICE_DATE = (By.CSS_SELECTOR, "#service_date")
    SERVICE_TIME = (By.CSS_SELECTOR, "#service_time")
    CONFIRM_SERVICE_BUTTON = (By.CSS_SELECTOR, "form > div > input[type='submit']")
    CONFIRM_CHANGE_SERVICE_MODAL_BUTTON = (By.CSS_SELECTOR, "div > div > input[id='submit']")
    SERVICE_ALERT = (By.CSS_SELECTOR, "div[class^='alert']")
    DOWN_ANCHOR = (By.CSS_SELECTOR, "span[class^='mb-3']")
    EDIT_SERVICE_BUTTON = (By.CSS_SELECTOR, "button[data-bs-target*='#editModal']")
    CHANGE_SERVICE_SUBMIT_BUTTON = (By.CSS_SELECTOR, "div[class='modal-footer'] > div > input")
    DELETE_SERVICE_BUTTON = (By.CSS_SELECTOR, "button[data-bs-target*='#deleteModal']")
    CONFIRM_DELETE_SERVICE_BUTTON = (By.CSS_SELECTOR, "form > input[class$='danger']")
    EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, "button[data-bs-target*='#profileModal']")
    EDIT_PHONE_NUM_FIELD = (By.CSS_SELECTOR, "form > div > input[type='tel']")
    SUBMIT_CHANGE_USER_DATA_BUTTON = (By.CSS_SELECTOR, "p > input[type='submit']")
