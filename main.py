import os
from dotenv import load_dotenv
from flask_openapi3 import OpenAPI, Info
from flask_jwt_extended import JWTManager
from flask import jsonify
from src.config.logging import logger  # Importer le logger configuré
from src.config.path_config import PathConfig  # Importer la classe PathConfig
from src.routers.auth_router import auth_bp
from src.routers.user_router import user_bp 
from flask_migrate import Migrate
from src.config.database import sync_engine, Base  # Importer la configuration synchrone de la base de données
from src.models import db  # Importer l'instance db de models
from src.exception.exceptions import UnauthorizedError, ValidationErrorResponse, UnexpectedError  # Importer les exceptions personnalisées
from src.config.jwt import JWTConfig  # Importer la configuration JWT

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Vérifier que SYNC_DATABASE_URL est bien défini
sync_database_url = os.getenv('SYNC_DATABASE_URL')
if not sync_database_url:
    raise RuntimeError("SYNC_DATABASE_URL is not set in the environment variables")

# Informations de l'API
info = Info(title="Authentication API", version="1.0.0")

# Configuration des schémas de sécurité pour JWT
jwt_security_scheme = {
    "type": "http",
    "scheme": "bearer",
    "bearerFormat": "JWT"
}
security_schemes = {"jwt": jwt_security_scheme}

app = OpenAPI(__name__, info=info, security_schemes=security_schemes)

# Configuration de la base de données (synchronisée pour les migrations)
app.config['SQLALCHEMY_DATABASE_URI'] = sync_database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration du JWTManager en utilisant JWTConfig
app.config['SECRET_KEY'] = JWTConfig.SECRET_KEY
app.config['JWT_SECRET_KEY'] = JWTConfig.SECRET_KEY
app.config['JWT_ALGORITHM'] = JWTConfig.ALGORITHM
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWTConfig.ACCESS_TOKEN_EXPIRE_MINUTES * 60

db.init_app(app)  # Initialiser SQLAlchemy avec l'application Flask
migrate = Migrate(app, db, directory='migrations')  # Initialiser Flask-Migrate

# Configuration de JWTManager
jwt = JWTManager(app)

# Enregistrement du blueprint
app.register_api(auth_bp)
app.register_api(user_bp)

@app.errorhandler(UnauthorizedError)
def handle_unauthorized_error(error):
    logger.error(f"Unauthorized error: {error.message}")
    response = {
        "code": error.code,
        "message": error.message
    }
    return jsonify(response), error.http_status

@app.errorhandler(ValidationErrorResponse)
def handle_validation_error(error):
    logger.error(f"Validation error: {error.errors}")
    response = {
        "code": error.code,
        "errors": error.errors
    }
    return jsonify(response), error.http_status

@app.errorhandler(UnexpectedError)
def handle_unexpected_error(error):
    logger.error(f"Unexpected error: {error.message}")
    response = {
        "code": error.code,
        "message": error.message
    }
    return jsonify(response), error.http_status

@app.errorhandler(Exception)
def handle_generic_exception(e):
    logger.error(f"An error occurred: {str(e)}", exc_info=True)
    error_response = UnexpectedError(message=str(e))
    response = {
        "code": error_response.code,
        "message": error_response.message
    }
    return jsonify(response), error_response.http_status

if __name__ == '__main__':
    app.run(debug=True)
