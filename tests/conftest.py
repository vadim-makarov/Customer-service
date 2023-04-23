"""Standard module for fixtures"""
import threading
from datetime import datetime
from typing import Generator

import allure
import pytest
from allure_commons.types import AttachmentType
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from app import db, create_app
from app.models import User, Service, Review
from config import TestConfig
from tests.helpers.helpers import generate_phone_number
from tests.ui_tests.pages.main_page import MainPage

fake = Faker()


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
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.set_window_size(1920, 1080)
    failed_before = request.session.testsfailed
    yield browser
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        screenshot(browser, test_name)
    browser.quit()


@pytest.fixture
def main_page(driver):
    """Открывает главную страницу"""
    page = MainPage(driver)
    page.open()
    return page


def screenshot(browser, name: str) -> None:
    """
    Gets a screenshot and attaches it to the report
    """
    allure.attach(browser.get_screenshot_as_png(), name=f"Screenshot {name}", attachment_type=AttachmentType.PNG)


@pytest.fixture
def user() -> User:
    """Returns a user instance for testing"""
    username = fake.name()
    phone = generate_phone_number()
    test_user = User(username=username, phone_number=phone)
    test_user.fake = fake
    return test_user


@pytest.fixture
def service(user):
    """Creates a user instance for testing"""
    db.session.add(user)
    db.session.commit()
    service = Service(service1='A jar of honey', service_date=datetime.now(),
                      service_time='10:00', user_id=user.id)
    db.session.add(service)
    db.session.commit()


@pytest.fixture
def new_service(user):
    """Returns a service for testing"""
    service = Service(service1='Chicken Burger', service2='Pepsi', service3='Delivery',
                      service_date=datetime.now(), service_time='14:00', user_id=user.id)
    return service


@pytest.fixture
def review(user):
    """Creates a service for testing"""

    db.session.add(user)
    db.session.commit()
    rev1 = Review(author=user.username, text='Sweeter than honey!', rating='Awesome!', author_id=user.id)
    rev2 = Review(author=user.username, text='Bitter than Kopalkhen', rating='Terrible!', author_id=user.id)
    rev3 = Review(author=user.username, text='Not bad', rating='So-so', author_id=user.id)
    db.session.add_all([rev1, rev2, rev3])
    db.session.commit()
