from flask import Flask
from src.routers.auth_router import auth_bp
from src.routers.user_router import user_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
