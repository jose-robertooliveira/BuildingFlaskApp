from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#criar uma secret-key no console python digitando import os > os.urando(12).hex()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '7f5358a3d3b7b00aeb4039dc'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market import routes