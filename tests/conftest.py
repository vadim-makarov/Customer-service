"""Standard module for fixtures"""
import threading
from typing import Generator

import pytest

from app import db, create_app
from config import TestConfig
from tests.config import URLs
from tests.models import generate_phone_number, NewUser, NewService, NewReview


@pytest.fixture(scope='session')
def app():
    """Creates a test instance of the app"""
    return create_app(TestConfig)


@pytest.fixture(scope='session', autouse=True)
def server(app) -> Generator:
    """Creates a database and runs app in new thread for testing UI"""
    app.app_context().push()
    db.create_all()
    app = threading.Thread(target=app.run)
    app.daemon = True
    yield app.start()
    db.drop_all()


@pytest.fixture
def user() -> NewUser:
    """Returns a user instance for testing"""
    test_user = NewUser()
    return test_user


@pytest.fixture
def phone_number() -> str:
    """Generates a random phone number"""
    number = generate_phone_number()
    return number


@pytest.fixture
def service():
    """Returns a service instance for testing"""
    service = NewService()
    return service


@pytest.fixture
def review():
    """Returns a review instance for testing"""
    review = NewReview()
    return review
