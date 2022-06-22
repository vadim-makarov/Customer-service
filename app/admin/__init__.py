from flask import Blueprint
from flask_admin.contrib.sqla import ModelView

from app.models import User, Service, Review

bp = Blueprint('administrator', __name__)

from app import db, admin
from app.admin import models, routes


admin.add_views(ModelView(User, db.session), ModelView(Service, db.session), ModelView(Review, db.session))
