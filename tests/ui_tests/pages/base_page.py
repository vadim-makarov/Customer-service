from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.ui_tests.pages.locators import LoginPageLocators


class BasePage:

    def __init__(self, driver: WebDriver, timeout: int = 60) -> None:
        self.driver = driver
        self.url = None
        self.wait = WebDriverWait(self.driver, timeout, poll_frequency=1)

    def open(self):
        """Открывает заданную страницу"""
        self.driver.get(self.url)

    def is_element_present(self, locator: tuple):
        """Проверяет наличие элемента на странице и возвращает bool"""
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
        except NoSuchElementException:
            return False
        return self

    def find_and_click_element(self, locator: tuple):
        """Ожидает появление элемента на странице, перемещает его в
        область видимости и кликает по нему"""
        self.wait.until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).click().perform()
        return self

    def find_element_and_input_data(self, locator: tuple, data: str):
        """Ожидает появления поля на странице, очищает его и вводит в текст"""
        self.wait.until(EC.element_to_be_clickable(locator))
        field = self.driver.find_element(*locator)
        field.send_keys(data)
        return self

    def go_to_the_next_window(self):
        """Ждет открытия нового окна и переключается на него"""
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        return self

    def go_to_the_prev_window(self):
        """Ожидает закрытия всех окон и переключается на первое окно"""
        self.wait.until(EC.number_of_windows_to_be(1))
        new_window = self.driver.window_handles[0]
        self.driver.switch_to.window(new_window)
        return self

    def should_be_some_page(self, page_name: str) -> bool:
        """Проверяет наличие имени страницы в текущем url"""
        self.wait.until(EC.url_contains(page_name))
        return page_name in self.driver.current_url

    def push_down_and_enter(self, locator: tuple):
        """выбирает первую посказку в выадающем меню"""
        self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        return self

    def get_text(self, locator: str) -> str:
        """возвращает текст из переданного элемента"""
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).text

    def switch_to_iframe(self, locator: tuple):
        """Ожидает появления iframe и переключается на него"""
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
        return self

    def input_data_wo_js(self, data: str):
        """Вводит посимвольно текст в выбранное ранее поле без JavaScript"""
        ActionChains(self.driver).send_keys(data).perform()
        return self

    def log_out_user(self):
        """Разлогинивает пользователя с подтверждением"""
        self.driver.find_element(*LoginPageLocators.LOGOUT_LINK).click()
        self.driver.find_element(*LoginPageLocators.LOGOUT_LINK_MODAL).click()
