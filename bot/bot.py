import asyncio
from aiogram import Bot
from config import BOT_TOKEN, CHAT_ID, CURRENCY_CODE, INTERVAL
from api import get_latest_currency_rates
from db import get_last_rate, save_rate
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)


async def currency_watcher():
    while True:
        try:
            new_buy_rate, new_sell_rate = await get_latest_currency_rates(CURRENCY_CODE)
            last_rate = await get_last_rate(CURRENCY_CODE)
            await save_rate(CURRENCY_CODE, new_buy_rate)

            if last_rate and last_rate != new_buy_rate:
                message = (f"Курс изменился с {last_rate['value']} "
                                   f"на {new_buy_rate} {CURRENCY_CODE}")
            else:
                message = f"Текущий курс: {new_buy_rate} {CURRENCY_CODE}"

            await bot.send_message(CHAT_ID, message)
        except Exception as e:
            logger.exception(e)

        await asyncio.sleep(INTERVAL)


async def main():
    await currency_watcher()

if __name__ == '__main__':
    asyncio.run(main())
