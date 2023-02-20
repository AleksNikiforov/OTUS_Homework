from sqlalchemy import Column, Text, String, Integer
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base,
    declared_attr,
)
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
import config


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User -> blog_users
        Author -> blog_authors
        """
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


async_engine = create_async_engine(url=config.DB_URL, echo=config.DB_ECHO)
Base = declarative_base(cls=Base)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)