from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from app.models import Currency

def get_all_rates():
    return Currency.query

class ExchangeForm(FlaskForm):
    from_currency = SelectField('From Currency', choices=['USD'])
    to_currency = QuerySelectField('To Currency', validators=[DataRequired()], query_factory=get_all_rates, get_label="currency_name")
    amount = StringField('Amount', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Convert')