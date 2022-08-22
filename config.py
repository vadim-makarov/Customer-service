import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    ENV = 'development'

    ### DATABASE ###
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I-cant-talk-about-this'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'user.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### SCHEDULER ###
    SCHEDULER_API_ENABLED = True

    ### ADMIN ###
    FLASK_ADMIN_SWATCH = 'united'

    ### SMS ###

    SMS_TOKEN = os.environ.get('SMS_TOKEN')

    ### MAIL ###
    MAIL_SERVER = 'smtp.mail.yahoo.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = os.environ.get('ADMINS')

    ### TeleBot ###
    BOT_TOKEN = os.environ.get('BOT_TOKEN')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.getcwd()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
