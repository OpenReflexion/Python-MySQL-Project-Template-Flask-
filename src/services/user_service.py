from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import SQLAlchemyError
from src.repositories.user_repository import get_user_by_email, create_user, update_user
from src.models.user_model import User, db

class UserService:
    @staticmethod
    def get_user_by_email(email):
        return get_user_by_email(email)

    @staticmethod
    def create_user(data):
        try:
            new_user = create_user(data)
            new_user.password = generate_password_hash(data['password'])
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_user_profile(email, data):
        user = get_user_by_email(email)
        if user:
            user = update_user(user, data)
            db.session.commit()
            return user
        return None
