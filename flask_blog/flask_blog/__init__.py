from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY'] = 'ae53bd80703afa7b52e730c4d0d9289b'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:john3333@localhost/testdb"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from flask_blog import route
