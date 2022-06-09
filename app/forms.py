from datetime import datetime

from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import StringField, SubmitField, TextAreaField, SelectField, TimeField, DateField
from wtforms.validators import ValidationError, EqualTo, Length, InputRequired, Regexp

from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(),
        Length(3, 20, message="Please provide a valid name"),
        Regexp("^[A-Za-z][A-Za-z0-9_ .]*$", 0,
               "Usernames must have only letters, " "numbers, "
               "dots or underscores")])
    phone_number = StringField('Phone number', validators=[InputRequired(), Length(10, 12),
                                                           Regexp(r"^\+(?:[0-9]●?){6,14}[0-9]$",
                                                                  message="Enter a valid phone number, like +55 555 "
                                                                          "555 555")])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField(validators=[InputRequired(),
                                       Length(3, 20, message="Please provide a valid name"),
                                       Regexp("^[A-Za-z][A-Za-z0-9_ .]*$", 0,
                                              "Usernames must have only letters, " "numbers, dots or underscores")])
    phone_number = StringField(validators=[InputRequired(), Length(10, 12),
                                           Regexp(r"^\+(?:[0-9]●?){6,14}[0-9]$",
                                                  message="Enter a valid phone number, like +55 555 555 555"),
                                           EqualTo("phone_number2",
                                                   message="Номера не совпадают!")])
    phone_number2 = StringField(validators=[InputRequired(), Length(10, 12)])
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
    phone_number = StringField(validators=[InputRequired(), Length(10, 12),
                                           Regexp(r"^\+(?:[0-9]●?){6,14}[0-9]$",
                                                  message="Enter a valid phone number, like +55 "
                                                          "555 555 555")])
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


class Services(FlaskForm):
    service1 = SelectField('Choose service:', choices=['Big-mak', 'Chicken Burger', 'Cheeseburger'])
    service2 = SelectField('Choose additional service:', choices=['', 'Coke-cola', 'Pepsi', 'Fanta'],
                           validate_choice=False)
    service3 = SelectField('Choose another additional service:', choices=['', 'At the place', 'To Go', 'Delivery'],
                           validate_choice=False)
    service_date = DateField('Choose the date', validators=[InputRequired()],
                             format='%Y-%m-%d', render_kw={"min": datetime.now().date()})
    service_time = TimeField('Choose the time', validators=[InputRequired()],
                             format='%H:%M', render_kw={"min": '10:00', 'max': '20:00', 'step': '1800'})
    submit = SubmitField('Enroll', render_kw={'class': 'btn btn-info'})
