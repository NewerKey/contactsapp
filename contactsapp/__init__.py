from sys import excepthook
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db= SQLAlchemy(app)
from contactsapp import routes

# for app to recognize and connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config ['SECRET_KEY'] = 'd76fbc47c80d4076ed4d653015ea2458a2cc2d58b965ab90e743ae40dcfdb92'


