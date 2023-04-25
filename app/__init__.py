"""Main init module contains create_app function"""
import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler

import telebot_router
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_manager
from flask_migrate import Migrate
from flask_paranoid import Paranoid
from flask_sqlalchemy import SQLAlchemy

import config
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
bootstrap = Bootstrap()
paranoid = Paranoid()
paranoid.redirect_view = '/'
login_manager.session_protection = None
bot = telebot_router.TeleBot(config.Config.BOT_TOKEN)


def create_app(config_class=Config):
    """Creates an instance of the app"""
    app: Flask = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.app_context().push()
    db.create_all()
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    paranoid.init_app(app)
    login.init_app(app)

    with app.app_context():

        from app.admin import bp as admin_bp
        app.register_blueprint(admin_bp, url_prefix='/admin')

        from app.errors import bp as errors_bp
        app.register_blueprint(errors_bp, url_prefix='/errors')

        from app.auth import bp as auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

        from app.user import bp as user_bp
        app.register_blueprint(user_bp, url_prefix='/user')

        from app.main import bp as main_bp
        app.register_blueprint(main_bp, url_prefix='/')

    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr=app.config['MAIL_USERNAME'],
                toaddrs=app.config['ADMINS'], subject='Customer Service Failure',
                credentials=auth, secure=())
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/customer_service.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('All good')

    return app


from app import models, sms
