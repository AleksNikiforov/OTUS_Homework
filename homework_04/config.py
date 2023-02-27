import os


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
DB_URL = "postgresql+asyncpg://username:passwd!@localhost:5432/blog"
DB_ECHO = False