from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    phone_number = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))  # TODO does this really need
    last_seen = db.Column(db.DateTime, default=datetime.now)
    services = db.relationship('Service', backref='client', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, phone_number):
        self.password_hash = generate_password_hash(phone_number)

    def check_password(self, phone_number):
        return check_password_hash(self.password_hash, phone_number)

    # def follow(self, user):
    #     if not self.is_following(user):
    #         self.followed.append(user)  # It will be service later
    #
    # def unfollow(self, user):
    #     if self.is_following(user):
    #         self.followed.remove(user)


class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(140))
    service_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # TODO service date\time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.service}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
