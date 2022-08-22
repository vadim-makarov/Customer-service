import pytest
import requests
from selenium import webdriver

# from app import create_app, db
# from config import TestConfig

URL = 'http://127.0.0.1:5000/main/index'


# @pytest.fixture(scope='session')
# def setUp():
#     app = create_app(TestConfig)
#     app_context = app.app_context()
#     app_context.push()
#     db.create_all()
#
#
# @pytest.fixture(scope='session')
# def tearDown():
#     db.session.remove()
#     db.drop_all()
#     app_context.pop()
#

@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope='class')
def status(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True
    return False
