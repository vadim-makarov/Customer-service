from flask_wtf import FlaskForm
from wtforms import StringField, TelField, SubmitField
from wtforms.validators import InputRequired, Regexp, ValidationError

from app.models import User


class MyLength:
    """
    Validates the length of a string.

    :param min:
        The minimum required length of the string. If not provided, minimum
        length will not be checked.
    :param max:
        The maximum length of the string. If not provided, maximum length
        will not be checked.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated using `%(min)d` and `%(max)d` if desired. Useful defaults
        are provided depending on the existence of min and max.

    When supported, sets the `minlength` and `maxlength` attributes on widgets.

    This is a fork of original class refactor for this case(conflict with Regexp
     when form pass the name with whitespaces in the end)
    """

    def __init__(self, min=-1, max=-1, message=None):
        assert (
                min != -1 or max != -1
        ), "At least one of `min` or `max` must be specified."
        assert max == -1 or min <= max, "`min` cannot be more than `max`."
        self.min = min
        self.max = max
        self.message = message
        self.field_flags = {}
        if self.min != -1:
            self.field_flags["minlength"] = self.min
        if self.max != -1:
            self.field_flags["maxlength"] = self.max

    def __call__(self, form, field):
        length = field.data.strip() and len(field.data.strip()) or 0
        if length >= self.min and (self.max == -1 or length <= self.max):
            return

        if self.message is not None:
            message = self.message

        elif self.max == -1:
            message = field.ngettext(
                f"Field must be at least {self.min} character long.",
                f"Field must be at least {self.min} characters long.",
            )
        elif self.min == -1:
            message = field.ngettext(
                f"Field cannot be longer than {self.max} character.",
                f"Field cannot be longer than {self.max} characters.",
            )
        elif self.min == self.max:
            message = field.ngettext(
                f"Field must be exactly {self.max} character long.",
                f"Field must be exactly {self.max} characters long.",
            )
        else:
            message = field.gettext(
                f"Field must be between {self.min} and {self.max} characters long."
            )

        raise ValidationError(message % {'min': self.min, 'max': self.max, 'length': length})


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(),
        MyLength(min=3, max=20, message="Please provide a valid name"),
        Regexp("^[A-Za-z][A-Za-z0-9_ .]*$", 0,
               "Usernames must have only latin letters, numbers, \
               dots or underscores")])
    phone_number = TelField('Phone number', validators=[InputRequired(), MyLength(min=10, max=12),
                                                        Regexp(r"^\+(?:[0-9]●?){10,12}[0-9]$",
                                                               message="Enter a valid phone number, like +55 555 "
                                                                       "555 555")])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),
                                                   MyLength(min=3, max=20, message="Please provide a valid name"),
                                                   Regexp("^[A-Za-z][A-Za-z0-9_ .]*$".strip(), 0,
                                                          "Usernames must have only latin letters, \
                                                            numbers, dots or underscores")])
    phone_number = TelField('Phone number', validators=[InputRequired(), MyLength(min=10, max=12),
                                                        Regexp(r"^\+(?:[0-9]●?){10,12}[0-9]$",
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
    code_input = StringField(validators=[MyLength(min=4, max=4)])
    register = SubmitField('Confirm')
