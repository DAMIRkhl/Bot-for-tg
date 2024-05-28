import random
import pyautogui
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from key import TOKEN, ID

bot = telebot.TeleBot(TOKEN)
number = 1


def hi():
    bot.send_message(ID, "PON")


@bot.message_handler(commands=["start"])
def start(message):
    baton = ReplyKeyboardMarkup()
    baton1 = KeyboardButton("/screenshot")
    baton2 = KeyboardButton("/casino")
    baton3 = KeyboardButton("/game_guess_the_number")
    baton.add(baton1, baton2)
    baton.add(baton3)

    bot.send_message(message.from_user.id,
                     "Hi welcome sorry for using english keyboard if you don't understand it i just don't have another keyboard",
                     reply_markup=baton)


@bot.message_handler(commands=["game_guess_the_number"])
def spike(message):
    baton = ReplyKeyboardMarkup()
    baton4 = KeyboardButton("/yes")
    baton5 = KeyboardButton("/no")
    baton.add(baton4, baton5)
    bot.send_message(message.from_user.id,
                     "think of the number between 1-20,is you number 1?",
                     reply_markup=baton)


@bot.message_handler(commands=["no"])
def start(message):
    global number
    number += 1
    bot.send_message(message.from_user.id,
                     f"is you number bigger than {number}?", )


@bot.message_handler(commands=["screenshot"])
def start(message):
    from subprocess import call
    if message.from_user.id == ID:
        call(['screencapture', 'screenshot.jpg'])
        bot.send_document(ID, open("/Users/olhakhalimova/Documents/python/GItHub/1bot/screenshot.jpg", "rb"))


@bot.message_handler(commands=["send"])
def start(message):
    import time
    # for i in range(20):
    #     time.sleep(2)
    #     bot.send_message(5277879764, "Я обещал")
    # text = message.text[5:]
    # grisha = 5277879764w
    # bot.send_message(grisha, text)


@bot.message_handler(content_types=["luck"])
def start(message):
    user_text = message.text  # здесь сообщение юзера! его нужно обрабатывать
    user_id = message.from_user.id
    print(user_text, user_id)


@bot.message_handler(commands=["casino"])
def start(message):
    casino = bot.send_dice(message.from_user.id, "🎰")
    if casino.dice.value in [43, 64, 22, 1]:
        pin = ["pin/photo_2024-05-07 16.43.11.jpeg", "pin/photo_2024-05-07 16.43.17.jpeg",
               "pin/photo_2024-05-07 16.43.27.jpeg", "pin/photo_2024-05-07 16.43.32.jpeg"]
        bot.send_photo(message.from_user.id, open(random.choice(pin), "rb"), caption="you are lucky")
    print(casino.dice.value)


# hi()
bot.polling()
