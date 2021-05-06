from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class ExchangeForm(FlaskForm):
    from_currency = SelectField('From Currency', choices=['USD'])
    to_currency = SelectField('To Currency', choices=['JPY', 'EUR', 'USD', 'BRL'])
    amount = StringField('Amount', validators=[DataRequired()])
    submit = SubmitField('Convert')