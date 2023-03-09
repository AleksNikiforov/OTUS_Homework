from sqlalchemy import Column, Text, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
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


async_engine = create_async_engine(url=config.SQLALCHEMY_DATABASE_URI, echo=config.DB_ECHO)
Base = declarative_base(cls=Base)
Session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    name = Column(String(40), unique=False, nullable=False)
    username = Column(String(40), unique=False, nullable=False)
    email = Column(String(40), default=False, nullable=False)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    title = Column(Text, nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    user_id = Column(Integer, ForeignKey("blog_users.id"), nullable=False, unique=False)

    user = relationship("User", back_populates="posts")
