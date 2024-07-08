import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    database_url = os.getenv("DATABASE_URL", "your_default_secret_key")
    secret_key = os.getenv("SECRET_KEY", "your_default_secret_key")
    algorithm = os.getenv("ALGORITHM", "your_default_secret_key")
    access_token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "your_default_secret_key")

    mailtrap_password = os.getenv("MAILTRAP_PASSWORD", "your_default_secret_key")
    mailtrap_username = os.getenv("MAILTRAP_USERNAME", "your_default_secret_key")


settings = Settings()

