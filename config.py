import os


class Config(object):
    SECRET_KEY = 'I-cant-talk-about-this'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'united'
    ### MAIL ###
    MAIL_SERVER = os.environ.get('smtp.mail.ru')
    MAIL_PORT = int(os.environ.get('465') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('zayaz28@mail.ru')
    MAIL_PASSWORD = os.environ.get('W08L770WbA8Ph058gkRw')
    ADMINS = ['zayaz2805@gmail.com']

