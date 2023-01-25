import threading

import pytest

from app import create_app, db
from config import TestConfig


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


@pytest.fixture()
def drop_db():
    db.drop_all()
    db.create_all()
