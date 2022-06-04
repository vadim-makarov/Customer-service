from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, EqualTo, Length, InputRequired, Regexp
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(),
        Length(3, 20, message="Please provide a valid name"),
        Regexp("^[A-Za-z][A-Za-z0-9_.]*$", 0, "Usernames must have only letters, " "numbers, dots or underscores")])
    phone_number = StringField('Phone number', validators=[InputRequired(), Length(10, 12),
                                                           Regexp("^\\+?[1-9][0-9]{10,12}$",
                                                                  message="Enter a valid Phone number")])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Как к вам обращаться?', validators=[InputRequired(),
                                                                Length(3, 20, message="Please provide a valid name"),
                                                                Regexp("^[A-Za-z][A-Za-z0-9_.]*$", 0,
                                                                       "Usernames must have only letters, " "numbers, dots or underscores")])
    phone_number = StringField('Телефон для связи:', validators=[InputRequired(), Length(10, 12),
                                                                 Regexp("^\\+?[1-9][0-9]{10,12}$",
                                                                        message="Enter a valid Phone number")])  # TODO make a phone number validator
    phone_number2 = StringField('Повторите телефон:', validators=[InputRequired(), Length(10, 12),
                                                                  EqualTo("phone_number",
                                                                          message="Номера не совпадают !")])
    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_username(username):  # if already exist
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    @staticmethod
    def validate_phone_number(phone_number):
        user = User.query.filter_by(phone_number=phone_number.data).first()
        if user is not None:
            raise ValidationError('Please use a different phone number.')


class EditProfileForm(FlaskForm):
    username = StringField('Как к вам обращаться?', validators=[InputRequired(),
                                                                Length(3, 20, message="Please provide a valid name"),
                                                                Regexp("^[A-Za-z][A-Za-z0-9_.]*$", 0,
                                                                       "Usernames must have only letters, " "numbers, dots or underscores")])
    phone_number = StringField('Телефон для связи:', validators=[InputRequired(), Length(10, 12),
                                                                 Regexp("^\\+?[1-9][0-9]{10,12}$",
                                                                        message="Enter a valid Phone number")])
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
                raise ValidationError('Please use a different phone number address.')
