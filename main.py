import telebot
from telebot import types
from telebot.types import WebAppInfo

API_TOKEN = '7790139740:AAHdVIGjirvYWR50eTKV6uYOhenAVPm9AcQ'  # Замените YOUR_API_TOKEN на ваш токен

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("Нажми меня!", web_app=WebAppInfo('https://thisismavver.github.io/server-site/'))
    keyboard.add(button)

    bot.send_message(message.chat.id, "Привет! Я простой бот. Нажми на кнопку ниже:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Нажми меня!")
def button_click(message):
    bot.reply_to(message, "Вы нажали на кнопку!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

@bot.message_handler(content_types=['web_app_data'])
def web_app(message: types.Message):
    a = message.web_app_data.data
    bot.reply_to(message, a)


if __name__ == '__main__':
    bot.polling()
