from flask import Blueprint, render_template, flash, request, redirect, url_for

from app import cache, db, hcaptcha
from app.main.forms import ExchangeForm
from app.currency import Curr
from app.models import Currency
import os
main = Blueprint('main', __name__)

request.headers['Content-Security-Policy'] = "script-src 'https://hcaptcha.com, https://*.hcaptcha.com'"

@cache.cached(timeout=14400, key_prefix='get_all_rates')
def updateRates():
    currency = Curr()
    exchange_rates = currency.getCurrencies()
    for rate in exchange_rates["rates"]:
        curr = Currency(currency_name=rate, currency_amount=exchange_rates["rates"][rate])  # find currency
        db.session.add(curr)
    db.session.commit()


@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():
    form = ExchangeForm()
    if form.validate_on_submit():
        if hcaptcha.verify():
            convert_to_curr = Curr(float(form.amount.data))  # Create object with currency in mind.
            curr_id = request.form['to_currency']
            currency = Currency.query.get(curr_id)  # Look in db for this currency.
            total_amount = convert_to_curr.toConvertCurrency(
                float(currency.currency_amount))  # uses the rate found in the database to do conversion.
            form.amount.data = total_amount
            flash('Converted successfully', 'success')
        else:
            flash('Please verify through HCaptcha!', 'danger')
            redirect(url_for('main.home'))
    googleapi = os.environ["GOOGLE_MAP_API"]
    return render_template('home.html', form=form, title='Home', googleapi=googleapi)


@main.route('/about')
def about():
    return render_template('about.html', title='About')
