from flask import Blueprint, current_app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import db
from app.models import User, Service, Review

bp = Blueprint('admin_app', __name__, url_prefix='/admin')
admin = Admin(current_app, name='Customer Service', template_mode='bootstrap4')
admin.name = 'Admin panel'
admin.add_views(ModelView(User, db.session), ModelView(Service, db.session), ModelView(Review, db.session))
from app.admin import models, routes
