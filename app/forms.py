from datetime import datetime

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField, TelField
from wtforms.validators import ValidationError, Length, InputRequired, Regexp

from app import db
from app.models import User, Service


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(),
        Length(3, 20, message="Please provide a valid name"),
        Regexp("^[A-Za-z][A-Za-z0-9_ .]*$", 0,
               "Usernames must have only letters, " "numbers, "
               "dots or underscores")])
    phone_number = TelField('Phone number', validators=[InputRequired(), Length(10, 12),
                                                        Regexp(r"^\+(?:[0-9]●?){6,14}[0-9]$",
                                                               message="Enter a valid phone number, like +55 555 "
                                                                       "555 555")])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField(validators=[InputRequired(),
                                       Length(3, 20, message="Please provide a valid name"),
                                       Regexp("^[A-Za-z][A-Za-z0-9_ .]*$", 0,
                                              "Usernames must have only letters, " "numbers, dots or underscores")])
    phone_number = TelField(validators=[InputRequired(), Length(10, 12),
                                        Regexp(r"^\+(?:[0-9]●?){6,14}[0-9]$",
                                               message="Enter a valid phone number, like +55555555555")])
    code = StringField(validators=[Length(4, message='Too short or too long. Please try again.')])
    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_username(self, username):  # if already exist
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    @staticmethod
    def validate_phone_number(self, phone_number):
        user = User.query.filter_by(phone_number=phone_number.data).first()
        if user is not None:
            raise ValidationError('Phone number already in use.')


class EditProfileForm(FlaskForm):
    username = StringField(validators=[InputRequired(),
                                       Length(3, 20, message="Please provide a valid name"),
                                       Regexp("^[A-Za-z][A-Za-z0-9_ .]*$", 0,
                                              "Usernames must have only letters, " "numbers, "
                                              "dots or underscores")])
    phone_number = TelField(validators=[InputRequired(), Length(10, 12),
                                        Regexp(r"^\+(?:[0-9]●?){6,14}[0-9]$",
                                               message="Enter a valid phone number, like +55"
                                                       "555555555")])
    about_me = TextAreaField('Дополнительная информация, пожелания:', validators=[Length(min=0, max=140)])
    submit = SubmitField('Подтвердить')

    def __init__(self, original_username, original_phone_number, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_phone_number = original_phone_number

    def validate_username(self, username):  # if already exist
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

    def validate_phone_number(self, phone_number):
        if phone_number.data != self.original_phone_number:
            user = User.query.filter_by(phone_number=self.phone_number.data).first()
            if user is not None:
                raise ValidationError('Phone number already in use.')


def validate_date_time(form, service_time):  # if already exist
    date_services = Service.query.filter_by(service_date=form.service_date.data).all()
    for service in date_services:
        if service.service_time == service_time.data:
            raise ValidationError('Please choose a different time.')


class Services(FlaskForm):
    service1 = SelectField('Choose service:', choices=['Big-mak', 'Chicken Burger', 'Cheeseburger'],
                           render_kw={'placeholder': '12341'})
    service2 = SelectField('Choose additional service:', choices=['', 'Coke-cola', 'Pepsi', 'Fanta'],
                           validate_choice=False)
    service3 = SelectField('Choose another additional service:', choices=['', 'At the place', 'To Go', 'Delivery'],
                           validate_choice=False)
    service_date = DateField('Choose the date', validators=[InputRequired()],
                             format='%d-%m-%Y', render_kw={"min": datetime.now().date()})
    service_time = SelectField('Choose the time', choices=['10:00', '12:00', '14:00', '16:00', '18:00'],
                               validators=[InputRequired(),
                                           validate_date_time])
    # TODO someting with the fuckn' time(str(datetime.now().time())[:5] > '14:00 --> True'
    submit = SubmitField('Enroll', render_kw={'class': 'btn btn-info'})


class CustomerServiceView(ModelView):
    form_base_class = SecureForm

    def __init__(self, *args, **kwargs):
        self._default_view = True
        super(CustomerServiceView, self).__init__(*args, **kwargs)
        self.admin = Admin()
        self.admin.add_view(ModelView(User, db.session))
        self.admin.add_view(ModelView(Service, db.session))

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
