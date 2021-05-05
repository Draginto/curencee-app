from flask import Blueprint, render_template, request, url_for

from app.main.forms import ExchangeForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    form = ExchangeForm()
    if form.validate_on_submit():

    return render_template('home.html', form=form)


@main.route('/about')
def about():
    return render_template('about.html', title='About')
