import threading

import pytest
from selenium import webdriver

from app import create_app
from config import TestConfig


@pytest.fixture(scope='session')
def app(request):
    from app import create_app
    return create_app(TestConfig)


@pytest.fixture
def test_client(request, app):
    client = app.test_client()
    client.__enter__()
    return client


@pytest.fixture(scope='session', autouse=True)
def server(app):
    app = threading.Thread(target=app.run)
    app.daemon = True
    yield app.start()


@pytest.fixture(scope='class')
def db():
    db.create_all(app=create_app(TestConfig))


@pytest.fixture(scope='class')
def browser():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    browser = webdriver.Chrome(options=op)
    yield browser
    browser.quit()
