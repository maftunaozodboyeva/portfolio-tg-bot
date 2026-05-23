import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	text = "Assalomu aleykum, mening portfolio botimga xush kelibsiz."
	# bot.reply_to(message, "Howdy, how are you doing?")
	keyboard = types.ReplyKeyboardMarkup()
	btn1 = types.KeyboardButton("About me")
	btn2 = types.KeyboardButton("Contact")
	btn3 = types.KeyboardButton("Projects")
	btn4 = types.KeyboardButton("Skills")	
	keyboard.add(btn1, btn2)
	keyboard.add(btn3, btn4)
	bot.send_message(message.chat.id, text, reply_markup=keyboard)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	if message.text == "about me":
# 		bot.send_message(message.chat.id, "Men Maftunaman💫")
# 	elif message.text == "contact":
# 		bot.send_message(message.chat.id, "Bu qism tez orada qo'shiladi📞")

@bot.message_handler(func=lambda message: message.text == "About me")
def aboutme_handler(message):
	bot.send_message(message.chat.id, "Men Maftunaman💫")

@bot.message_handler(func=lambda message: message.text == "Contact")
def contact_handler(message):
	keyboard = types.InlineKeyboardMarkup()
	btn1 = types.InlineKeyboardButton(text = "Telegram", url="https://t.me/shakhnozame")
	keyboard.add(btn1)
	text = "Men bilan bog'lanish uchun quyidagi havola ustiga bosing"
	bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Projects")
def projects_handler(message):
	keyboard = types.InlineKeyboardMarkup()
	btn1 = types.InlineKeyboardButton(text = "GitHub", url="https://github.com/maftunaozodboyeva")
	keyboard.add(btn1)
	text = "Mening loyihalarim haqida ma'lumot"
	bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Skills")
def skills_handler(message):
	keyboard = types.InlineKeyboardMarkup()
	btn1 = types.InlineKeyboardButton(text = "About all me", url="https://https://loveable-maftuna-portfolio.lovable.app/")
	keyboard.add(btn1)
	text = "Mening ko'nikmalarim haqida ma'lumot"
	bot.send_message(message.chat.id, text, reply_markup=keyboard)

bot.infinity_polling()