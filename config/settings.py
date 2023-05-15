import os
from decouple import config
from sqlalchemy.dialects.postgresql import psycopg2
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')


class Settings:
    PROJECT_NAME: str = "Todo"
    PROJECT_VERSION: str = "1.0.0"

    USE_POSTGRESQL_DB: str = config("USE_POSTGRESQL_DB")
    POSTGRES_USER: str = config("POSTGRES_USER")
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = config('POSTGRES_SERVER')
    POSTGRES_DB: str = config("POSTGRES_DB")
    POSTGRES_PORT: str = config("POSTGRES_PORT")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()
