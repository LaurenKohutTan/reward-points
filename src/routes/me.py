from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import app
from database import Student

# Returns the current user's information
@app.route('/api/me')
@jwt_required()
def get_me():
    id = get_jwt_identity()
    student = Student.query.filter_by(id=id).first()
    return jsonify(student.as_json())
