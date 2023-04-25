"""Blueprint init module"""

from flask import Blueprint

bp = Blueprint('user_blueprint', __name__)

from app.user import forms, routes
