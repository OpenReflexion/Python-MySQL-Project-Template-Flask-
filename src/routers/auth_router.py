from flask_openapi3 import APIBlueprint, Tag
from flask import jsonify
from pydantic import ValidationError
from http import HTTPStatus
from src.controllers.auth_controller import AuthController  # Importer AuthController
from src.schemas.auth_schemas import RegisterSchema, LoginSchema, ForgotPasswordSchema, ResetPasswordSchema
from src.config.logging import logger  # Importer le logger configuré
from src.exception.exceptions import UnauthorizedError, ValidationErrorResponse, UnexpectedError  # Importer les exceptions personnalisées

auth_tag = Tag(name="auth", description="Authentication related endpoints")
security = [{"jwt": []}]

auth_bp = APIBlueprint(
    'auth_bp',
    __name__,
    abp_tags=[auth_tag],
    abp_security=security,
)

@auth_bp.post('/auth/register', tags=[auth_tag], summary="Register a new user")
def register_user_route(body: RegisterSchema):
    """
    User registration endpoint
    """
    try:
        return AuthController.register_user(body.model_dump())
    except ValidationError as err:
        logger.error(f"[AUTHENTIFICATION][REGISTER] : Validation error: {err.errors()}", exc_info=True)
        raise ValidationErrorResponse(errors=err.errors())
    except Exception as e:
        logger.error(f"[AUTHENTIFICATION][REGISTER] : Error: {e}", exc_info=True)
        raise UnexpectedError(message=str(e))

@auth_bp.post('/auth/login', tags=[auth_tag], summary="Login a user")
def login_user_route(body: LoginSchema):
    """
    User login endpoint
    """
    try:
        return AuthController.login_user(body.model_dump())
    except ValidationError as err:
        logger.error(f"[AUTHENTIFICATION][LOGIN] : Validation error: {err.errors()}", exc_info=True)
        raise ValidationErrorResponse(errors=err.errors())
    except Exception as e:
        logger.error(f"[AUTHENTIFICATION][LOGIN] : Error: {e}", exc_info=True)
        raise UnexpectedError(message=str(e))

@auth_bp.post('/auth/forgot-password', tags=[auth_tag], summary="Forgot password")
def forgot_password_route(body: ForgotPasswordSchema):
    """
    Forgot password endpoint
    """
    try:
        return AuthController.forgot_password(body.model_dump())
    except ValidationError as err:
        logger.error(f"[AUTHENTIFICATION][FORGOT_PASSWORD] : Validation error: {err.errors()}", exc_info=True)
        raise ValidationErrorResponse(errors=err.errors())
    except Exception as e:
        logger.error(f"[AUTHENTIFICATION][FORGOT_PASSWORD] : Error: {e}", exc_info=True)
        raise UnexpectedError(message=str(e))

@auth_bp.post('/auth/reset-password', tags=[auth_tag], summary="Reset password")
def reset_password_route(body: ResetPasswordSchema):
    """
    Reset password endpoint
    """
    try:
        return AuthController.reset_password(body.model_dump())
    except ValidationError as err:
        logger.error(f"[AUTHENTIFICATION][RESET_PASSWORD] : Validation error: {err.errors()}", exc_info=True)
        raise ValidationErrorResponse(errors=err.errors())
    except Exception as e:
        logger.error(f"[AUTHENTIFICATION][RESET_PASSWORD] : Error: {e}", exc_info=True)
        raise UnexpectedError(message=str(e))
