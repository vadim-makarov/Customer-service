import threading

import pytest
from selenium import webdriver

from app import create_app, db
from config import TestConfig

pytest_plugins = []  # put your custom fixture *.py files here as a string without extension


@pytest.fixture(scope='session')
def app(request):
    return create_app(TestConfig)


@pytest.fixture(scope='session')
def app_test_client(request, app):
    client = app.test_client()
    client.__enter__()
    return client


@pytest.fixture(scope='session', autouse=True)
def server(app):
    app.app_context().push()
    db.create_all()
    app = threading.Thread(target=app.run)
    app.daemon = True
    yield app.start()
    db.drop_all()


@pytest.fixture(scope='class')
def browser():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    # browser = webdriver.Chrome(options=op)
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
