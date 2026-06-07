import telebot
from telebot import types

TOKEN = "8811157992:AAFxsfGVx2tfZ7hJl86dhujDLkWQjyCxXoc"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    anime_btn = types.KeyboardButton("🎬 Anime")
    kino_btn = types.KeyboardButton("🎥 Kino")
    yordam_btn = types.KeyboardButton("ℹ️ Yordam")

    markup.add(anime_btn, kino_btn)
    markup.add(yordam_btn)

    text = """
🎬 Assalomu alaykum!

🌸 AniLife Bot 🌸

🤖 Eng sara animelar
🎞 HD sifatdagi qismlar
⚡ Tez va qulay foydalanish

👇 Kerakli bo'limni tanlang
"""

    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def buttons(message):
    if message.text == "🎬 Anime":
        bot.send_message(message.chat.id, "Anime bo'limiga xush kelibsiz!")

    elif message.text == "🎥 Kino":
        bot.send_message(message.chat.id, "Kino bo'limiga xush kelibsiz!")

    elif message.text == "ℹ️ Yordam":
        bot.send_message(
            message.chat.id,
            "Anime yoki kino nomini yuboring. Yordam kerak bo'lsa admin bilan bog'laning."
        )

print("Bot ishga tushdi...")
bot.infinity_polling()
