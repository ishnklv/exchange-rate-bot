import asyncio

from db import create_init_tables


async def init_db():
    await create_init_tables()

if __name__ == '__main__':
    asyncio.run(init_db())
