from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import app
from database import Student

@app.route('/api/me')
@jwt_required()
def me():
    id = get_jwt_identity()
    student = Student.query.filter_by(id=id).first()

    return jsonify({
        "id": student.id,
        "name": student.name,
        "picture": student.picture,
        "points": student.points,
    })