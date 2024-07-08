from pydantic import BaseModel, EmailStr, constr

class RegisterSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class ForgotPasswordSchema(BaseModel):
    email: EmailStr

class ResetPasswordSchema(BaseModel):
    token: str
    new_password: str
