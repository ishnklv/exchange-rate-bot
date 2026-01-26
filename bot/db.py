import aiosqlite

from config import DB_FILE


async def create_init_tables():
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute("""
            create table if not exists rates (
                id integer primary key autoincrement,
                currency varchar not null,
                value decimal not null,
                timestamp datetime default CURRENT_TIMESTAMP
            )
        """)
        await db.commit()


async def save_rate(currency: str, value: float):
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute(
            "insert into rates (currency, value) values (?, ?)",
            (currency, value)
        )
        await db.commit()


async def get_last_rate(currency: str):
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute(
            "select currency, value from rates where currency=? order by timestamp desc limit 1",
            (currency,)
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                return {"currency": row[0], "value": row[1]}
            return None


async def delete_all_rates(currency: str=None):
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute(
            "delete from rates where currency=?",
            (currency,)
        )
        await db.commit()
