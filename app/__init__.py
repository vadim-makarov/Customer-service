import telebot
from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_manager
from flask_migrate import Migrate
from flask_paranoid import Paranoid
from flask_sqlalchemy import SQLAlchemy
from smsapi.client import SmsApiPlClient

import config
from config import Config

app = Flask(__name__)  # TODO redo all into app_factory
app.config.from_object(Config)

###  DataBase ###
db = SQLAlchemy(app)
db.create_all()
migrate = Migrate(app, db)

### Security ###
login = LoginManager(app)
login.login_view = 'login'
paranoid = Paranoid(app)
paranoid.redirect_view = '/'
login_manager.session_protection = None

### TeleBot/SMS ###
client = SmsApiPlClient(access_token=config.Config.SMS_TOKEN)
bot = telebot.TeleBot(config.Config.BOT_TOKEN, parse_mode=None)
admin = Admin(app, name='Customer Service', template_mode='bootstrap4')

### Blueprints ###
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp, url_prefix='/errors')

from app.admin import bp as admin_bp
app.register_blueprint(admin_bp, url_prefix='/auth')


### Frontend ###
Bootstrap(app)

from app import routes, models

# ###  Celery ###
# app = Celery()
