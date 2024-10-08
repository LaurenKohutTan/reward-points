from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import app, db
from database import Student, Transaction
import config

# Returns a list of all students if the user is a teacher
@app.route('/api/students')
@jwt_required()
def get_students():
    id = get_jwt_identity()
    if not id in config.teacher_ids:
        return 'Access Denied', 400

    students = Student.query.filter(Student.id.notin_(config.teacher_ids), Student.active == True).all()
    return jsonify([student.as_json() for student in students])

@app.route('/api/save', methods=['POST'])
@jwt_required()
def post_save():
    id = get_jwt_identity()
    if not id in config.teacher_ids:
        return 'Access Denied', 400

    data = request.get_json()

    for id in data:
        student = Student.query.get(id)
        if student:
            student.points += data[id]
            db.session.add(Transaction(student.id, data[id]))
    db.session.commit()

    return jsonify(data)

@app.route('/api/delete', methods=['POST'])
@jwt_required()
def post_delete():
    id = get_jwt_identity()
    if not id in config.teacher_ids:
        return 'Access Denied', 400

    data = request.get_json()
    students = Student.query.filter(Student.id.in_(data)).all()
    for student in students:
        student.active = False
    db.session.commit()

    return jsonify([student.id for student in students])
