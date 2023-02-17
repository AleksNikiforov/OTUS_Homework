import aiohttp
import asyncio
"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
- доработайте модуль `jsonplaceholder_requests`:
    - установите значения в константы `USERS_DATA_URL` и `POSTS_DATA_URL` (ресурсы нужно взять отсюда https://jsonplaceholder.typicode.com/)
    - создайте асинхронные функции для выполнения запросов к данным ресурсам (используйте `aiohttp`)
        - рекомендуется добавить базовые функции для запросов, которые будут переиспользованы (например `fetch_json`)
"""


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_users_data(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result: dict = await response.json()
            return result


async def get_posts_data(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result: dict = await response.json()
            return result


async def main():
    results = await asyncio.gather(
        get_users_data(USERS_DATA_URL),
        get_posts_data(POSTS_DATA_URL),
    )
    return results


if __name__ == "__main__":
    asyncio.run(main())