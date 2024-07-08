# src/repositories/user_repository.py

from src.models.user_model import User

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_user(data):
    new_user = User(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        email=data.get('email'),
        password=data.get('password')
    )
    return new_user

def update_user(user, data):
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.location = data.get('location', user.location)
    user.title = data.get('title', user.title)
    user.description = data.get('description', user.description)
    user.country = data.get('country', user.country)
    user.phone_number = data.get('phone_number', user.phone_number)
    return user
