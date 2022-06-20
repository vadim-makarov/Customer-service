import telebot
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_manager
from flask_paranoid import Paranoid
from flask_sqlalchemy import SQLAlchemy

import config
from config import Config

app = Flask(__name__)  # TODO redo all into app_factory
app.config.from_object(Config)

###  DataBase ###
db = SQLAlchemy(app)
db.create_all()

### Security ###
login = LoginManager(app)
login.login_view = 'login'
paranoid = Paranoid(app)
paranoid.redirect_view = '/'
login_manager.session_protection = None
bot = telebot.TeleBot(config.Config.BOT_TOKEN, parse_mode=None)

### Frontend ###
Bootstrap(app)

from app import routes, models, errors

###  ADMIN  ###
admin = Admin(app, name='Customer Service', template_mode='bootstrap4')

from app.models import User, Service, Review

admin.add_views(ModelView(User, db.session), ModelView(Service, db.session), ModelView(Review, db.session))

