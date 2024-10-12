from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from config.database.data import DataBase
import os

db = DataBase(os.path.join(os.getcwd(), "config", "database", "data.db"))

# _________________________Настройка Бота____________________________
admin_id = [1956728833]
token = "8021474411:AAEAhXY1gXggT3LK9cJe115ereY8qax5Qyc"
# ___________________________________________________________________

# ___________________________________________________________________
balance_for_referral = 40
balance_for_click = 1
money_name = "HiddenCoin"
bot_username = "HiddenCOINru_bot"
min_withdraw = 8000
redirect_link = "https://t.me/HiddenCOINru_bot"
min_referrer_withdraw = 5
feedback_link = "https://t.me/HiddenCOINru_bot"
# ___________________________________________________________________
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
