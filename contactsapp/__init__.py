from sys import excepthook
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db= SQLAlchemy(app)

# for app to recognize and connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from contactsapp import routes