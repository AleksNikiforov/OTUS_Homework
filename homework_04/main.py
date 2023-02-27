import asyncio
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from models import User, Post, async_engine, Session, Base
from jsonplaceholder_requests import get_users_data, get_posts_data


async def create_tables():
  async with async_engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
  async with async_engine.begin() as conn:
      await conn.run_sync(Base.metadata.drop_all)


async def create_user(session: AsyncSession, name: str, username: str, email: str):
  user = User(name=name, username=username, email=email)
  session.add(user)

    
async def create_post(session: AsyncSession, user_id: int, title: str, body: str):
  post = Post(user_id=user_id, title=title, body=body)
  session.add(post)


async def async_main():
  #await drop_tables()
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
          await create_post(session=session, user_id=post.get('userId'), title=post.get('title'), body=post.get('body'))
        await session.commit()


async def main():
  await async_main()


if __name__ == "__main__":
  asyncio.run(main())
