import os
import telebot
from telebot import types
from flask import Flask
from threading import Thread

TOKEN = "8811157992:AAGhHV8MntMhffe1PT2UPSHNNqzNSaBnElE"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    anime_btn = types.KeyboardButton("🎬 Anime")
    kino_btn = types.KeyboardButton("🎥 Kino")
    yordam_btn = types.KeyboardButton("ℹ️ Yordam")

    markup.add(anime_btn, kino_btn)
    markup.add(yordam_btn)

    bot.send_message(
        message.chat.id,
        "🌸 AniLife Bot 🌸\n\n👇 Kerakli bo'limni tanlang",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def buttons(message):

    if message.text == "🎬 Anime":
        bot.send_message(
            message.chat.id,
            "Anime kodini yuboring:\n\n"
            "1 - Solo Leveling"
        )

    elif message.text == "1":

        markup = types.InlineKeyboardMarkup()

        watch_btn = types.InlineKeyboardButton(
            "▶️ Ko'rish",
            url="https://t.me/+FBTBF49JT6IyNzUy"
        )

        markup.add(watch_btn)

        bot.send_message(
            message.chat.id,
            "⚔️ Solo Leveling\n\n"
            "⭐ Janr: Action, Fantasy\n"
            "📅 Yili: 2024\n\n"
            "🎬 Barcha qismlar kanalda mavjud.",
            reply_markup=markup
        )

    elif message.text == "🎥 Kino":
        bot.send_message(
            message.chat.id,
            "🎥 Kino bo'limi hozircha bo'sh."
        )

    elif message.text == "ℹ️ Yordam":
        bot.send_message(
            message.chat.id,
            "Anime yoki kino kodini yuboring."
        )

@app.route("/")
def home():
    return "AniLife Bot ishlayapti!"

def run_bot():
    print("Bot ishga tushdi...")
    bot.infinity_polling(skip_pending=True)

if __name__ == "__main__":
    Thread(target=run_bot).start()
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
