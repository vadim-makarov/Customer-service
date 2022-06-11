from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db.create_all()
login = LoginManager(app)
login.login_view = 'login'

Bootstrap(app)

from app import routes, models, errors

###  ADMIN  ###
admin = Admin(app, name='Customer Service', template_mode='bootstrap3')

from app.models import User, Service

admin.add_views(ModelView(User, db.session), ModelView(Service, db.session))
