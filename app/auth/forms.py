from flask_wtf import FlaskForm
from wtforms import StringField, TelField, SubmitField
from wtforms.validators import InputRequired, Length, Regexp, ValidationError

from app.models import User


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
    confirm = SubmitField('Send SMS code')

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


class SMSForm(FlaskForm):
    code_input = StringField(validators=[Length(4, 4)])
    register = SubmitField('Confirm')