"""Contains fixtures for unit testing"""

import pytest

from app import create_app, db
from config import TestConfig


@pytest.fixture(scope='session', autouse=True)
def app():
    """Creates a test instance of the app and the database"""
    app = create_app(TestConfig)
    db.create_all()
    yield app
    db.drop_all()


@pytest.fixture()
def client(app):
    """Creates a test client"""
    return app.test_client()


@pytest.fixture()
def drop_db():
    """Recreates DB"""
    db.drop_all()
    db.create_all()
