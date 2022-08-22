import pytest
import requests
from selenium import webdriver

from app import db, create_app
from config import TestConfig

URL = 'http://127.0.0.1:5000/main/index'

@pytest.fixture(scope='session')
def setUp():
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()
    db.create_all()


@pytest.fixture(scope='session')
def tearDown():
    db.session.remove()
    db.drop_all()
    app.app_context.pop()


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def status():
    r = requests.get(URL)
    if r.status_code == 200:
        return True
    return False