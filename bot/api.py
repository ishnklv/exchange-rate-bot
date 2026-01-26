import httpx
from config import VALUTA_API_URL


async def get_currency_history_rates(currency_code: str):
    url = f"{VALUTA_API_URL}/api/rates/history.json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params={"currency": currency_code})
        data = response.json()

        if response.status_code != 200:
            raise ValueError(f"Invalid response code: {response.status_code}")

        if data['error']:
            raise ValueError(f"Api error: {data['message']}")

        return data


async def get_latest_currency_rates(currency_code: str):
    history_rates = await get_currency_history_rates(currency_code)
    latest_buy_rate = history_rates['data']['buy'][-1][1]
    latest_sell_rate = history_rates['data']['sell'][-1][1]

    return latest_buy_rate, latest_sell_rate

