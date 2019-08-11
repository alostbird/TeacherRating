# Using Flask WTF (WT Forms) to represent web forms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    # Automatic resolving of email
    email = StringField('Email', validators=[DataRequired(), Email()])
    dept = SelectField('Department', choices=[(
        'cse', 'CSE'), ('it', 'IT'), ('swe', 'Software')], validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # Check if both passwords are the same
    password2 = PasswordField('Repeat Password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('E-mail is already in use. Try again.')
