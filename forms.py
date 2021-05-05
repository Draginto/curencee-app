from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    """Attrs: used for field names"""
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Exists Already! Please try another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken! Please try another one.')


class LoginForm(FlaskForm):
    """Attrs: used for field names"""
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ExchangeForm(FlaskForm):
    from_currency = SelectField('From Currency', choice=['USD', 'EUR'])
    to_currency = SelectField('To Currency', choices=['JPY', 'BRL'])
    amount = StringField('Amount', validators=[DataRequired()])
    submit = SubmitField('Convert')