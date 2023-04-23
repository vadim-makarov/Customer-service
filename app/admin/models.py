"""Contains an admin panel class"""
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm

from app import db
from app.models import User, Service, Review


class CustomerServiceView(ModelView):
    """Redefined an admin model view class"""
    form_base_class = SecureForm

    def __init__(self, model, session):
        super().__init__(model, session)
        self._default_view = True
        self.admin = Admin()
        self.admin.add_view(ModelView(User, db.session))
        self.admin.add_view(ModelView(Service, db.session))
        self.admin.add_view(ModelView(Review, db.session))
