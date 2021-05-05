from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5c753b9873cba5d4f2cb3415a4b1d62f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

if __name__ == '__main__':
    app.run(debug=True)
