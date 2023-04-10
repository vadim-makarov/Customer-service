import threading

import pytest

import app
from app import create_app, db
from config import TestConfig


@pytest.fixture(scope='session')
def app() -> app:
    return create_app(TestConfig)


@pytest.fixture(scope='session', autouse=True)
def app():
    app = create_app(TestConfig)
    db.create_all()
    yield app
    db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture(scope='class', autouse=True)
def server(app):
    app.app_context().push()
    db.create_all()
    app = threading.Thread(target=app.run)
    app.daemon = True
    yield app.start()
    db.drop_all()


@pytest.fixture()
def drop_db():
    db.drop_all()
    db.create_all()

