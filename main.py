from flask_openapi3 import OpenAPI, Tag, Info
from flask_jwt_extended import JWTManager
from flask import jsonify
from src.config.logging import logger  # Importer le logger configuré
from src.config.path_config import PathConfig  # Importer la classe PathConfig
from src.routers.auth_router import auth_bp

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
