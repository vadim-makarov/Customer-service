"""Contains fixtures for unit testing"""

import pytest

from app import create_app, db
from app.models import Service, Review, User
from config import TestConfig
from tests.models import NewReview, NewService


@pytest.fixture(scope='session', autouse=True)
def app():
    """Creates a test instance of the app and the database"""
    new_app = create_app(TestConfig)
    db.create_all()
    yield new_app
    db.drop_all()


@pytest.fixture()
def client(app):
    """Creates a test client"""
    return app.test_client()


@pytest.fixture
def user_in_db(user) -> User:
    """Returns a user instance for testing"""
    test_user = User(username=user.username, phone_number=user.phone_number)
    db.session.add(test_user)
    db.session.commit()
    return test_user


@pytest.fixture
def service_in_db(user_in_db):
    """Creates a user instance for testing"""
    service = NewService()
    new_service = Service(service1=service.service1, service_date=service.service_date,
                          service_time=service.service_time, user_id=user_in_db.id)
    db.session.add(new_service)
    db.session.commit()


@pytest.fixture
def review_in_db(user_in_db):
    """Creates a service for testing"""
    review = NewReview()
    rev1 = Review(author=user_in_db.username, text=review.text, rating='Awesome!', author_id=user_in_db.id)
    rev2 = Review(author=user_in_db.username, text=review.text, rating='Terrible!', author_id=user_in_db.id)
    rev3 = Review(author=user_in_db.username, text=review.text, rating='So-so', author_id=user_in_db.id)
    db.session.add_all([rev1, rev2, rev3])
    db.session.commit()
