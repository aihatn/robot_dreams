import os
from dotenv import load_dotenv

load_dotenv()

URL_IP = "https://api.ipify.org/"
API_KEY = os.getenv("TOMORROW_API_KEY")

if not API_KEY:
    raise ValueError("Chybí TOMORROW_API_KEY v .env souboru")
