import telebot
from telebot import types

TOKEN = "8811157992:AAGhHV8MntMhffe1PT2UPSHNNqzNSaBnElE"

bot = telebot.TeleBot(TOKEN)

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
        bot.send_message(message.chat.id, "Anime kodini yuboring. Masalan: 1")

    elif message.text == "1":
        bot.send_message(
            message.chat.id,
            "⚔️ Solo Leveling\n\n⭐ Janr: Action, Fantasy\n📅 Yili: 2024"
        )

print("Bot ishga tushdi...")
bot.infinity_polling()

