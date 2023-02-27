import os


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@localhost:5432/blog"
DB_URL = "postgresql+asyncpg://username:passwd!@localhost:5432/blog"
DB_ECHO = False