"""Contains fixtures for unit testing"""
from datetime import datetime

import pytest

from app import create_app, db
from app.models import Service, Review
from config import TestConfig


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
def service(user):
    """Creates a user instance for testing"""
    db.session.add(user)
    db.session.commit()
    new_service = Service(service1='A jar of honey', service_date=datetime.now(),
                          service_time='10:00', user_id=user.id)
    db.session.add(new_service)
    db.session.commit()


@pytest.fixture
def review(user):
    """Creates a service for testing"""
    db.session.add(user)
    db.session.commit()
    rev1 = Review(author=user.username, text='Sweeter than honey!', rating='Awesome!', author_id=user.id)
    rev2 = Review(author=user.username, text='Bitter than Kopalkhen', rating='Terrible!', author_id=user.id)
    rev3 = Review(author=user.username, text='Not bad', rating='So-so', author_id=user.id)
    db.session.add_all([rev1, rev2, rev3])
    db.session.commit()
