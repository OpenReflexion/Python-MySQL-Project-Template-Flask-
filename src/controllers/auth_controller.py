from flask import jsonify
from flask_jwt_extended import decode_token
from sqlalchemy.exc import SQLAlchemyError
from http import HTTPStatus
from src.models.user_model import User
from src.services.auth_service import AuthService

def register_user(data):
    try:
        new_user = AuthService.register_user(data)
        return jsonify({"message": "User registered successfully"}), HTTPStatus.CREATED
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

def login_user(data):
    user = AuthService.authenticate_user(data['email'], data['password'])
    if user:
        access_token_expires = timedelta(minutes=30)
        access_token = AuthService.create_access_token(identity=user.email, expires_delta=access_token_expires)
        return jsonify({"access_token": access_token, "token_type": "bearer"}), HTTPStatus.OK
    return jsonify({"message": "Invalid credentials"}), HTTPStatus.UNAUTHORIZED

def forgot_password(data):
    user = User.query.filter_by(email=data['email']).first()
    if user:
        reset_token = AuthService.generate_reset_password_token(user)
        # Here you would normally send an email with the reset token
        return jsonify({"reset_token": reset_token}), HTTPStatus.OK
    return jsonify({"message": "Email not found"}), HTTPStatus.NOT_FOUND

def reset_password(data):
    try:
        decoded_token = decode_token(data['token'])
        user = User.query.filter_by(email=decoded_token['sub']).first()
        if user:
            AuthService.reset_password(user.email, data['new_password'])
            return jsonify({"message": "Password reset successfully"}), HTTPStatus.OK
        return jsonify({"message": "Invalid token"}), HTTPStatus.UNAUTHORIZED
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
