from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    reference = db.Column(db.String(255), nullable=True, unique=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(128), nullable=True, unique=True)
    password = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=True)
    title = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    country = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(255), nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
