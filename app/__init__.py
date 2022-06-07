from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
Bootstrap4(app)
from app import routes, models

