from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from config import secret_key, db_address

app = Flask(__name__)
app.instance_path = "./instance"
app.template_folder = "./templates"
app.static_folder = "./static"

app.secret_key = secret_key
app.config["JWT_SECRET_KEY"] = secret_key
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = db_address
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']

db = SQLAlchemy(app)
jwt = JWTManager(app)
