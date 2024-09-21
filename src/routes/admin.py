from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import app
from database import Student
import config

@app.route('/api/students')
@jwt_required()
def get_students():
    id = get_jwt_identity()
    if not id in config.teacher_ids:
        return 'Access Denied', 400

    students = Student.query.all()
    return jsonify([student.as_json() for student in students])