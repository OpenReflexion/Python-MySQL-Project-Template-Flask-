from src.models.user_model import User

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_user(data):
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password']
    )
    return new_user
