from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv


app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI = str(os.getenv('DATABASE_URI')),
    SQLALCHEMY_TRACK_MODIFICATINOS=False,
    SECRET_KEY=str(os.getenv('SECRET_KEY')))

db = SQLAlchemy(app)


from application import routes
