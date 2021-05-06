from flask import Blueprint, render_template, request, url_for

from app.main.forms import ExchangeForm
from app.currency import Currency

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():
    form = ExchangeForm()
    if form.validate_on_submit():
        currency = Currency(float(form.amount.data), form.from_currency.data)
        total_amount = currency.toCurrency(form.to_currency.data)
        form.amount.data = total_amount
    return render_template('home.html', form=form)


@main.route('/about')
def about():
    return render_template('about.html', title='About')
