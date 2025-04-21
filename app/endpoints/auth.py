from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import SignUpRequest, SignInRequest, TokenResponse, SignUpResponse
from app.db.session import get_db
from app.crud import auth as auth_crud
from app.core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/signup", response_model=SignUpResponse)
def signup(payload: SignUpRequest, db: Session = Depends(get_db)):
    if auth_crud.get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = auth_crud.create_user(db, payload.email, payload.password, payload.first_name, payload.last_name)
    token = create_access_token(data={"sub": user.email})
    return {
        "access_token": token,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

@router.post("/signin", response_model=TokenResponse)
def signin(payload: SignInRequest, db: Session = Depends(get_db)):
    user = auth_crud.get_user_by_email(db, payload.email)
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token}
