from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)