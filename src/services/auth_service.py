from flask_jwt_extended import create_access_token
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import SQLAlchemyError
from src.models.user_model import User, db
from src.repositories.user_repository import get_user_by_email, create_user

class AuthService:
    @staticmethod
    def create_access_token(identity, expires_delta):
        return create_access_token(identity=identity, expires_delta=expires_delta)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return check_password_hash(hashed_password, plain_password)

    @staticmethod
    def get_password_hash(password):
        return generate_password_hash(password)

    @staticmethod
    def authenticate_user(email, password):
        user = get_user_by_email(email)
        if user and AuthService.verify_password(password, user.password):
            return user
        return None

    @staticmethod
    def register_user(data):
        try:
            new_user = create_user(data)
            new_user.password = AuthService.get_password_hash(data['password'])
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def generate_reset_password_token(user):
        expires_delta = timedelta(hours=1)
        reset_token = create_access_token(identity=user.email, expires_delta=expires_delta)
        return reset_token

    @staticmethod
    def reset_password(email, new_password):
        user = get_user_by_email(email)
        if user:
            user.password = AuthService.get_password_hash(new_password)
            db.session.commit()
            return user
        return None
