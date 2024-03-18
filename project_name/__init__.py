import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt

# from flask_bootstrap import Bootstrap4  # bootstrap = Bootstrap4(app)
from flask_bootstrap import Bootstrap5  # bootstrap = Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Apples'

# configure the SQLite database, relative to the app instance folder
pwd = os.getcwd()
"""  Valid SQLite URL forms are:
        sqlite:///:memory: (or, sqlite://)
        sqlite:///relative/path/to/file.db
        sqlite:////absolute/path/to/file.db
"""
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{pwd}/site.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# initialize the app with the extension
with app.app_context():
    db.init_app(app)

# bootstrap = Bootstrap4(app)
bootstrap = Bootstrap5(app)

bcrypt = Bcrypt(app)

from project_name import routes
