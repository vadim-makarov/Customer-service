from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm

from app import db
from app.models import User, Service, Review


class CustomerServiceView(ModelView):
    form_base_class = SecureForm

    def __init__(self, *args, **kwargs):
        self._default_view = True
        super(CustomerServiceView, self).__init__(*args, **kwargs)
        self.admin = Admin()
        self.admin.add_view(ModelView(User, db.session))
        self.admin.add_view(ModelView(Service, db.session))
        self.admin.add_view(ModelView(Review, db.session))

# class MyModelView(BaseModelView):
#     column_exclude_list = User.password_hash
#
#
# class UserView(ModelView):
#     form_overrides = dict(title=SelectField)
#     form_args = dict(
#         # Pass the choices to the `SelectField`
#         title=dict(
#             choices=['11:00', '14:00']
#         ))
#
#     def __init__(self, session, **kwargs):
#         super(UserView, self).__init__(User, session, **kwargs)
#
#     def is_accessible(self):
#         return login.current_user.is_authenticated()
#
#     def create_form(self):
#         form = Services()
#         form.service_time.choices = ['15:00', '25:00']
#         return form
