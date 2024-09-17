from flask_sqlalchemy import SQLAlchemy

from app import db

class Student(db.Model):
    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    picture = db.Column(db.Text)
    points = db.Column(db.Integer)

    def __init__(self, id, name, picture):
        self.id = id
        self.name = name
        self.picture = picture
        self.points = 0
