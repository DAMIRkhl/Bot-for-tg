import  telebot

from key import TOKEN, ID

bot=telebot.TeleBot(TOKEN)
bot.send_message(ID,"PON")
