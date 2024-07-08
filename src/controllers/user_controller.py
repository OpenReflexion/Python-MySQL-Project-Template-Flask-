from flask import jsonify
from src.services.user_service import UserService
from http import HTTPStatus

class UserController:
    @staticmethod
    def get_user_profile(email):
        user = UserService.get_user_by_email(email)
        if user:
            return jsonify({
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "location": user.location,
                "title": user.title,
                "description": user.description,
                "country": user.country,
                "phone_number": user.phone_number
            }), HTTPStatus.OK
        return jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND

    @staticmethod
    def update_user_profile(email, data):
        user = UserService.update_user_profile(email, data)
        if user:
            return jsonify({"message": "User profile updated successfully"}), HTTPStatus.OK
        return jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND
