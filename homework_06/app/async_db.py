import asyncio
from sqlalchemy.ext.asyncio import (AsyncSession)
from models import User, Post, async_engine, Session, Base
from jsonplaceholder_requests import get_users_data, get_posts_data



async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, name: str, username: str, email: str):
    user = User(name=name, username=username, email=email)
    session.add(user)

    
async def create_post(session: AsyncSession, title: str, body: str):
    post = Post(title=title, body=body)
    session.add(post)


async def async_get_data():
    await create_tables()
    users_data, posts_data = await asyncio.gather(
          get_users_data(),
          get_posts_data(),
      )
    async with Session() as session:
          for user in users_data:
            await create_user(session=session, name=user.get('name'), username=user.get('username'), email=user.get('email'))
          await session.commit()
          for post in posts_data:
            await create_post(session=session, title=post.get('title'), body=post.get('body'))
          await session.commit()
