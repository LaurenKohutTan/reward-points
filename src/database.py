from flask_sqlalchemy import SQLAlchemy

from app import db

class Student(db.Model):
    name = db.Column(db.String())
    period = db.Column(db.Integer())
    email = db.Column(db.String())
    points = db.Column(db.Integer())

    def __init__(self, name, period, email):
        self.name = name
        self.period = period
        self.email = email
        self.points = 0
