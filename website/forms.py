from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class UserInput(FlaskForm):
    stock = StringField('Stock',
                           validators=[DataRequired(), Length(min=2, max=20)])
    start = StringField('Start Date (Please enter in YYYY, MM, DD format)',
                           validators=[DataRequired(), Length(min=2, max=20)])
    finish = StringField('Finish Date (Please enter in YYYY, MM, DD format)',
                           validators=[DataRequired(), Length(min=2, max=20)])
    
    enter = SubmitField('Search Up')
    