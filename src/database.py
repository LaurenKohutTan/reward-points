from flask_sqlalchemy import SQLAlchemy

from app import db

class Student(db.Model):
    # Google user ID
    id = db.Column(db.Text, primary_key=True)
    # Full name
    name = db.Column(db.Text)
    # Link to their profile picture
    picture = db.Column(db.Text)
    # Number of reward points
    points = db.Column(db.Integer)

    def __init__(self, id, name, picture):
        self.id = id
        self.name = name
        self.picture = picture
        self.points = 0

    def as_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture": self.picture,
            "points": self.points,
        }
