from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
# banco de dados sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fakepinterest.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SECRET_KEY"] = "super secret key"
app.config["UPLOAD_FOLDER"] = "fakepinterest/static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from fakepinterest import routes  # noqa: E402, F401
