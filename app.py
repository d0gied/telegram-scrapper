from aiogram import Bot, Dispatcher, types
import asyncio

from src.config import Config
from src.scrapper.service import app

if __name__ == "__main__":
    print("Starting bot...")
    app.run()
