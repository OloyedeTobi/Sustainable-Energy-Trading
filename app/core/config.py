from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Literal

class Settings(BaseSettings):
    env: Literal["development", "production"] = "development"
    app_name: str = "FastAPI Auth"
    debug: bool = True
    database_url: str
    secret_key: str
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    settings = Settings()
    if settings.env == "production":
        settings.Config.env_file = "prod.env"
        return Settings(_env_file="prod.env")
    return settings
