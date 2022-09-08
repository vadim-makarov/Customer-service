import random
import string
import threading

import pytest
from selenium import webdriver

from app import create_app, db
from app.models import User
from config import TestConfig

pytest_plugins = []  # put your custom fixture *.py files here as a string without extension


@pytest.fixture(scope='session')
def app():
    return create_app(TestConfig)


@pytest.fixture(scope='session')
def app_test_client(app):
    client = app.test_client()
    client.__enter__()
    return client


@pytest.fixture(scope='class', autouse=True)
def server(app):
    db.drop_all()
    app.app_context().push()
    db.create_all()
    app = threading.Thread(target=app.run)
    app.daemon = True
    yield app.start()
    db.drop_all()


@pytest.fixture(params=["chrome", "firefox", "edge"], scope='class')
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
        case "edge":
            options = webdriver.EdgeOptions()
            options.headless = toggle
            browser = webdriver.Edge(options=options)
    request.cls.driver = browser
    yield browser
    browser.quit()


@pytest.fixture()
def user(app):
    username = ''.join(random.sample(string.ascii_lowercase, 8))
    phone = '+' + ''.join(random.sample(string.digits * 3, 12))
    user = User(username=username, phone_number=phone)
    return user
#
#
# @pytest.fixture()
# def service(test_db, user):
#     service = Service(username=user.username, service1='A jar of honey', service_date=datetime.now(),
#                       service_time='10:00')
#     test_db.session.add(service)
#     test_db.session.commit()
#     return service
#
#
# @pytest.fixture()
# def review(test_db, user):
#     review = Review(user.username, text='Sweeter than honey!', rating='Awesome!')
#     test_db.session.add(review)
#     test_db.session.commit()
#     return review
