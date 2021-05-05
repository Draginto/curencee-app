from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.currency import Currency

class ExchangeForm(FlaskForm):
    from_currency = SelectField('From Currency', choices=['USD', 'EUR'])
    to_currency = SelectField('To Currency', choices=['JPY', 'BRL'])
    amount = StringField('Amount', validators=[DataRequired()])
    submit = SubmitField('Convert')