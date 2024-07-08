from flask_openapi3 import APIBlueprint, Tag
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from src.controllers.user_controller import UserController  # Importer le contrôleur User

user_tag = Tag(name="user", description="User related endpoints")
security = [{"jwt": []}]

user_bp = APIBlueprint(
    'user_bp',
    __name__,
    abp_tags=[user_tag],
    abp_security=security,
)

@user_bp.get('/user/profile', tags=[user_tag], summary="Get user profile")
@jwt_required()
def get_user_profile():
    """
    Get user profile endpoint
    """
    user_email = get_jwt_identity()
    return UserController.get_user_profile(user_email)

@user_bp.put('/user/profile', tags=[user_tag], summary="Update user profile")
@jwt_required()
def update_user_profile():
    """
    Update user profile endpoint
    """
    user_email = get_jwt_identity()
    data = request.get_json()
    return UserController.update_user_profile(user_email, data)
