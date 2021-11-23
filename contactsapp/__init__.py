from sys import excepthook
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db= SQLAlchemy(app)
from contactsapp import routes



