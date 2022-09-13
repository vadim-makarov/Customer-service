import random
import string
import threading
from datetime import datetime

import pytest
from selenium import webdriver

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


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def browser(request):
    toggle = True  # changes the headless parameter for all browsers
    match request.param:
        case "chrome":
            options = webdriver.ChromeOptions()
            options.headless = toggle
            browser = webdriver.Chrome(options=options)
        case "firefox":
            options = webdriver.FirefoxOptions()
            options.headless = toggle
            browser = webdriver.Firefox(options=options)
    request.cls.driver = browser
    yield browser
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


