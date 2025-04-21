from pydantic import BaseModel, EmailStr


class SignUpRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class SignInRequest(BaseModel):
    email: EmailStr
    password: str

class SignUpResponse(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    access_token: str
    token_type: str = "bearer"

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
