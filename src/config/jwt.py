import os
from dotenv import load_dotenv

load_dotenv()

class JWTConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    ALGORITHM = os.getenv("ALGORITHM", "your_default_secret_key")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "your_default_secret_key")

JWTConfig = JWTConfig()
