import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I-cant-talk-about-this'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
