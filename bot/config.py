import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
VALUTA_API_URL = "https://valuta.kg"
INTERVAL = 300
DB_FILE = 'db.sqlite3'
CURRENCY_CODE = 'rub'
