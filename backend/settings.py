import os

os.getenv("DB_USER", "POSTGRES")

DB_USER = os.getenv("DB_USER", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_HOST", "5432")
DB_PASSWORD = os.getenv("DB_HOST", "default_password")

POSTGRES_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"

SESSION_EXPIRE_SECONDS = 60 * 60 * 24 * 3
