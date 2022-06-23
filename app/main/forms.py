from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, RadioField
from wtforms.validators import Length, InputRequired


class Reviews(FlaskForm):
    text = TextAreaField('Enter your text here:', validators=[InputRequired(), Length(min=2, max=300)])
    rating = RadioField('Rating', validators=[InputRequired()],
                        choices=['Terrible!', 'Bad', 'So-so', 'Good', 'Awesome!'])
    send_review = SubmitField('Confirm')
