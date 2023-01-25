import random
import string
from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app import db
from app.models import User, Service, Review


@pytest.fixture(params=["chrome"])
def browser(request) -> webdriver:
    """
    the fixture downloads the latest driver and creates the browser instance with passed options
    """
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    browser.set_window_size(1920, 1080)
    failed_before = request.session.testsfailed
    yield browser
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        screenshot(browser, test_name)
    browser.quit()


def screenshot(browser, name: str) -> None:
    """
    Gets a screenshot and attaches it to the report
    """
    allure.attach(browser.get_screenshot_as_png(), name=f"Screenshot {name}", attachment_type=AttachmentType.PNG)


@pytest.fixture()
def user():
    username = ''.join(random.sample(string.ascii_lowercase, 8))
    phone = '+' + ''.join(random.sample(string.digits * 3, 11))
    user = User(username=username, phone_number=phone)
    return user


@pytest.fixture()
def service(user):
    db.session.add(user)
    db.session.commit()
    service = Service(service1='A jar of honey', service_date=datetime.now(),
                      service_time='10:00', user_id=user.id)
    db.session.add(service)
    db.session.commit()


@pytest.fixture()
def review(user):
    db.session.add(user)
    db.session.commit()
    rev1 = Review(author=user.username, text='Sweeter than honey!', rating='Awesome!', author_id=user.id)
    rev2 = Review(author=user.username, text='Bitter than Kopalkhen', rating='Terrible!', author_id=user.id)
    rev3 = Review(author=user.username, text='Not bad', rating='So-so', author_id=user.id)
    db.session.add_all([rev1, rev2, rev3])
    db.session.commit()
