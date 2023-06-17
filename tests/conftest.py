"""Standard module for fixtures"""
import threading
from typing import Generator

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from app import db, create_app
from config import TestConfig
from tests.ui_tests.pages.main_page import MainPage
from tests.ui_tests.src.config import URLs
from tests.ui_tests.src.models import TestUser


@pytest.fixture(scope='session')
def app():
    """Creates a test instance of the app"""
    return create_app(TestConfig)


@pytest.fixture(scope='session', autouse=True)
def server(app) -> Generator:
    """Creates a database and runs app in new thread for testing UI"""
    app.app_context().push()
    db.create_all()
    app = threading.Thread(target=app.run)
    app.daemon = True
    yield app.start()
    db.drop_all()


@pytest.fixture
def driver(request) -> Generator:
    """
    the fixture downloads the latest driver and creates the browser instance with passed options
    """
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    failed_before = request.session.testsfailed
    yield browser
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        screenshot(browser, test_name)
    browser.quit()


@pytest.fixture
def main_page(driver) -> MainPage:
    """Открывает главную страницу"""
    page = MainPage(driver)
    page.open(URLs.main_page_url)
    return page


def screenshot(browser: WebDriver, name: str) -> None:
    """
    Gets a screenshot and attaches it to the report
    """
    allure.attach(browser.get_screenshot_as_png(), name=f"Screenshot {name}", attachment_type=AttachmentType.PNG)


@pytest.fixture
def user() -> TestUser:
    """Returns a user instance for testing"""
    test_user = TestUser()
    return test_user
