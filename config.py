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

    ### CELERY ###
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://default:redispw@localhost:49156")
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://default:redispw@localhost:49156f")

    ### REDIS ###
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://default:redispw@localhost:49156'

    ### ADMIN ###
    FLASK_ADMIN_SWATCH = 'united'

    ### SMS ###

    SMS_TOKEN = "bLQCWwiUPawU5xKF4DJE7uZh5lHCrlRjcTwjdXGz"

    ### MAIL ###
    MAIL_SERVER = 'smtp.mail.ru'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'zayaz28@mail.ru'
    MAIL_PASSWORD = 'pVs3wVQVmE5k1eKNuqei'
    ADMINS = ['zayaz2805@gmail.com']

    ### TeleBot ###
    BOT_TOKEN = "5499247330:AAFXWyZzxMP1PZsfIKd_M6duJFKs37jcbFE"


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
