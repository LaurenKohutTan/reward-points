import datetime

from flask_sqlalchemy import SQLAlchemy

from app import db

class Student(db.Model):
    # Google user ID
    id = db.Column(db.Text, primary_key=True)
    # Student's email
    email = db.Column(db.Text)
    # Student's name
    full_name = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    # Link to their profile picture
    picture = db.Column(db.Text)
    # Number of reward points
    points = db.Column(db.Integer)
    # If the student has been deleted or not
    active = db.Column(db.Boolean)

    def __init__(self, id, email, first_name, last_name, name, picture):
        self.id = id
        self.email = email
        self.full_name = name
        self.first_name = first_name
        self.last_name = last_name
        self.picture = picture
        self.points = 0
        self.active = True

    def as_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": {
                "full": self.full_name,
                "first": self.first_name,
                "last": self.last_name,
            },
            "picture": self.picture,
            "points": self.points,
            "active": self.active,
        }

# Represents someone gaining or losing points
class Transaction(db.Model):
    # The user who gained or lost points
    user_id = db.Column(db.Text, db.ForeignKey("student.id"), primary_key=True)
    # The timestamp of the operation
    date = db.Column(db.DateTime, primary_key=True)
    # The number of points gained or lost
    points = db.Column(db.Integer)

    def __init__(self, user_id, points):
        self.user_id = user_id
        self.date = datetime.datetime.now()
        self.points = points

    def as_json(self):
        return {
            "date": self.date.strftime("%m/%d/%Y %H:%M:%S"),
            "delta": self.points,
        }
