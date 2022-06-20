class Config(object):
    SECRET_KEY = 'I-cant-talk-about-this'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
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
