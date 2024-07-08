import os
from dotenv import load_dotenv
from flask_openapi3 import OpenAPI, Info
from flask_jwt_extended import JWTManager
from flask import jsonify
from src.config.logging import logger  # Importer le logger configuré
from src.config.path_config import PathConfig  # Importer la classe PathConfig
from src.routers.auth_router import auth_bp
from flask_migrate import Migrate
from src.config.database import sync_engine, Base  # Importer la configuration synchrone de la base de données
from src.models import db  # Importer l'instance db de models

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

db.init_app(app)  # Initialiser SQLAlchemy avec l'application Flask
migrate = Migrate(app, db, directory='migrations')  # Initialiser Flask-Migrate

# Configuration de JWTManager
jwt = JWTManager(app)

# Enregistrement du blueprint
app.register_api(auth_bp)

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"An error occurred: {str(e)}", exc_info=True)
    return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
