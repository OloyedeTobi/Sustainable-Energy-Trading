from fastapi import FastAPI
from app.endpoints import auth

app = FastAPI()

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
