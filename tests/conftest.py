import random
import string
import threading
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

from app import create_app, db
from app.models import User, Service, Review
from config import TestConfig

pytest_plugins = []  # put your custom fixture *.py files here as a string without extension

capabilities = {
    "browserName": "chrome",
    "browserVersion": "105.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}


@pytest.fixture(scope='session')
def app():
    return create_app(TestConfig)


@pytest.fixture(scope='class', autouse=True)
def server(app):
    app.app_context().push()
    db.create_all()
    app = threading.Thread(target=app.run)
    app.daemon = True
    yield app.start()
    db.drop_all()

    # @pytest.fixture()
    # def browser():
    #     browser = webdriver.Remote(
    #         command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)
    #     yield browser
    #     browser.quit()


@pytest.fixture(params=["chrome", "firefox"])
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


@pytest.fixture()
def drop_db():
    db.drop_all()
    db.create_all()
