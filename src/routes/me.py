from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import app
from database import Student, Transaction

# Returns the current user's information
@app.route('/api/me')
@jwt_required()
def get_me():
    id = get_jwt_identity()
    student = Student.query.filter_by(id=id).first()
    history = Transaction.query.filter_by(user_id=id).all()
    assert student is not None

    out = student.as_json()
    out["history"] = [transaction.as_json() for transaction in history]

    return jsonify(out)
