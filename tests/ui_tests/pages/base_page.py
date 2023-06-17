"""Module contains Base class"""

from __future__ import annotations

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Contains common methods"""

    MAIN_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > a')
    FEATURES_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > ul > li:nth-child(1) > a')
    PRICING_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > ul > li:nth-child(2) > a')
    REVIEWS_PAGE_LINK = (By.CSS_SELECTOR, 'body > header > div > div > ul > li:nth-child(3) > a')
    LOGIN_LINK = (By.CSS_SELECTOR, ".btn-outline-light")
    REGISTER_LINK = (By.CSS_SELECTOR, 'a.btn:nth-child(2)')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'button[data-bs-target="#logoutModal"]')
    LOGOUT_LINK_MODAL = (By.CSS_SELECTOR, '#logoutModal > div > div > div.modal-footer > a')
    SUCCESS_REGISTER_ALERT = (By.CSS_SELECTOR, "div[role='alert']")
    USER_BUTTON = (By.CSS_SELECTOR, "div[class='text-end'] > a")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout, poll_frequency=1)

    def open(self, url: str) -> None:
        """Открывает заданную страницу"""
        self.driver.get(url)

    def is_element_present(self, locator: tuple, err_msg: str) -> BasePage | OSError:
        """Проверяет наличие элемента на странице"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(err_msg)
        return self

    def find_and_click_element(self, locator: tuple) -> BasePage:
        """Ожидает появление элемента на странице, перемещает его в
        область видимости и кликает по нему"""
        ActionChains(self.driver).move_to_element(self.wait.until(
            EC.element_to_be_clickable(locator))).click().perform()
        return self

    def find_element_and_input_data(self, locator: tuple, data: str) -> BasePage:
        """Ожидает появления поля на странице, очищает его и вводит в текст"""
        self.wait.until(EC.element_to_be_clickable(locator))
        field = self.driver.find_element(*locator)
        field.send_keys(data)
        return self

    def select_value(self, locator: tuple, value: str) -> BasePage:
        """Выбирает значение по value из дропдауна"""
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_value(value)
        return self

    def go_to_the_next_window(self) -> BasePage:
        """Ждет открытия нового окна и переключается на него"""
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        return self

    def go_to_the_prev_window(self) -> BasePage:
        """Ожидает закрытия всех окон и переключается на первое окно"""
        self.wait.until(EC.number_of_windows_to_be(1))
        new_window = self.driver.window_handles[0]
        self.driver.switch_to.window(new_window)
        return self

    def push_down_and_enter(self, locator: tuple) -> BasePage:
        """Выбирает первую подсказку в выпадающем меню"""
        self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        return self

    def get_text(self, locator: tuple) -> str:
        """Возвращает текст из переданного элемента"""
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).text

    def input_data_wo_js(self, data: str) -> BasePage:
        """Вводит посимвольно текст в выбранное ранее поле без JavaScript"""
        ActionChains(self.driver).send_keys(data).perform()
        return self

    def log_out_user(self) -> BasePage:
        """Разлогинивает пользователя с подтверждением"""
        self.find_and_click_element(self.LOGOUT_LINK) \
            .find_and_click_element(self.LOGOUT_LINK_MODAL)
        return self
