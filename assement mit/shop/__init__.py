from flask import Flask
import os 
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 899

# get abs path to the papp dir to create the db here
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'shop.db')
db = SQLAlchemy(app)




login_manager = LoginManager()
login_manager.init_app(app)

from shop import routes
