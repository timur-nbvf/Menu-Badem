import os
import asyncio
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Открыть меню", web_app=WebAppInfo(url="https://timur-nbvf.github.io/Badem-menu/NewIndex.html"))
    )
    await message.answer("Нажми на кнопочку ниже, чтобы заказать еду 🍲", reply_markup=keyboard)

@app.post("/send-order")
async def send_order(request: Request):
    data = await request.json()
    order_list = "\n".join(data.get("order", []))
    text = f"Новый заказ:\n\n{order_list}"
    try:
        await bot.send_message(chat_id=CHAT_ID, text=text)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(dp.start_polling())
