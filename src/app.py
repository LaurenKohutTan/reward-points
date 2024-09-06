from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import secret_key, db_address

app = Flask(__name__)
app.instance_path = "./instance"
app.template_folder = "../templates"
app.static_folder = "../static"
app.secret_key = secret_key

app.config["SQLALCHEMY_DATABASE_URI"] = db_address
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# see:
# https://github.com/aspiringLich/amplitude/blob/main/src/routes/auth.rs
# https://github.com/Sigma-8214/CompSci-RP-Website
