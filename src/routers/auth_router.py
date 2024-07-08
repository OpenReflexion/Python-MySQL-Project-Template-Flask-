from flask_openapi3 import APIBlueprint, Tag
from flask import jsonify
from pydantic import BaseModel, ValidationError, EmailStr, Field
from http import HTTPStatus
from src.controllers.auth_controller import register_user, login_user, forgot_password, reset_password
from src.schemas.auth_schemas import RegisterSchema, LoginSchema, ForgotPasswordSchema, ResetPasswordSchema
from src.config.logging import logger  # Importer le logger configuré

auth_tag = Tag(name="auth", description="Authentication related endpoints")
security = [{"jwt": []}]

auth_bp = APIBlueprint(
    'auth_bp',
    __name__,
    abp_tags=[auth_tag],
    abp_security=security,
)

class Unauthorized(BaseModel):
    code: int = Field(-1, description="Status Code")
    message: str = Field("Unauthorized!", description="Exception Information")

# Routes utilisant flask-openapi3 pour la documentation et la validation
@auth_bp.post('/auth/register', tags=[auth_tag], summary="Register a new user")
def register_user_route(body: RegisterSchema):
    """
    User registration endpoint
    """
    try:
        response = register_user(body.dict())
        logger.info("[AUTHENTIFICATION][REGISTER] : User registered successfully")
        return jsonify(response), HTTPStatus.CREATED
    except ValidationError as err:
        logger.error(f"[AUTHENTIFICATION][REGISTER] : Validation error: {err.errors()}", exc_info=True)
        return jsonify(err.errors()), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(f"[AUTHENTIFICATION][REGISTER] : Error: {e}", exc_info=True)
        return jsonify({"error": "An unexpected error occurred"}), HTTPStatus.INTERNAL_SERVER_ERROR

@auth_bp.post('/auth/login', tags=[auth_tag], summary="Login a user")
def login_user_route(body: LoginSchema):
    """
    User login endpoint
    """
    try:
        response = login_user(body.dict())
        logger.info("[AUTHENTIFICATION][LOGIN] : User logged in successfully")
        return jsonify(response), HTTPStatus.OK
    except ValidationError as err:
        logger.error(f"[AUTHENTIFICATION][LOGIN] : Validation error: {err.errors()}", exc_info=True)
        return jsonify(err.errors()), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(f"[AUTHENTIFICATION][LOGIN] : Error: {e}", exc_info=True)
        return jsonify({"error": "An unexpected error occurred"}), HTTPStatus.INTERNAL_SERVER_ERROR

@auth_bp.post('/auth/forgot-password', tags=[auth_tag], summary="Forgot password")
def forgot_password_route(body: ForgotPasswordSchema):
    """
    Forgot password endpoint
    """
    try:
        response = forgot_password(body.dict())
        logger.info("[AUTHENTIFICATION][FORGOT_PASSWORD] : Password reset link sent")
        return jsonify(response), HTTPStatus.OK
    except ValidationError as err:
        logger.error(f"[AUTHENTIFICATION][FORGOT_PASSWORD] : Validation error: {err.errors()}", exc_info=True)
        return jsonify(err.errors()), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(f"[AUTHENTIFICATION][FORGOT_PASSWORD] : Error: {e}", exc_info=True)
        return jsonify({"error": "An unexpected error occurred"}), HTTPStatus.INTERNAL_SERVER_ERROR

@auth_bp.post('/auth/reset-password', tags=[auth_tag], summary="Reset password")
def reset_password_route(body: ResetPasswordSchema):
    """
    Reset password endpoint
    """
    try:
        response = reset_password(body.dict())
        logger.info("[AUTHENTIFICATION][RESET_PASSWORD] : Password has been reset")
        return jsonify(response), HTTPStatus.OK
    except ValidationError as err:
        logger.error(f"[AUTHENTIFICATION][RESET_PASSWORD] : Validation error: {err.errors()}", exc_info=True)
        return jsonify(err.errors()), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(f"[AUTHENTIFICATION][RESET_PASSWORD] : Error: {e}", exc_info=True)
        return jsonify({"error": "An unexpected error occurred"}), HTTPStatus.INTERNAL_SERVER_ERROR
