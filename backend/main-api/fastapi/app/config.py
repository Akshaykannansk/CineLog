import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.fastapi_env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "FastAPI with PostgreSQL"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
