"""Contains a DB schema"""

from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class User(UserMixin, db.Model):
    """Describes a User table"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    phone_number = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.String, default=datetime.now().date())
    services = db.relationship('Service', backref='client', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}-->{self.phone_number}'

    def set_password(self, phone_number):
        """Generates a hash from the passed phone number"""
        self.password_hash = generate_password_hash(phone_number)

    def check_password(self, phone_number):
        """Checks if passed phone number matches to a password hash"""
        return check_password_hash(self.password_hash, phone_number)


class Review(db.Model):
    """Describes a Review table"""
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), default='Happy client')
    text = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.String(1), nullable=False)
    review_date = db.Column(db.String, index=True, default=datetime.now().date())
    author_id = db.Column(db.String(64), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.rating}-->{self.text}-->{self.review_date}'


class Service(db.Model):
    """Describes a Service table"""
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    service1 = db.Column(db.String(60), index=True, nullable=False)
    service2 = db.Column(db.String(60), index=True)
    service3 = db.Column(db.String(60), index=True)
    service_date = db.Column(db.Date, index=True, nullable=False)
    service_time = db.Column(db.String, index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.id, self.service1, self.service2, self.service3, self.service_time}'


@login.user_loader
def load_user(user_id: str) -> User:
    """Returns a logged user"""
    return db.session.get(User, int(user_id))
