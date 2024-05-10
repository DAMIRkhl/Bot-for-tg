import random
import pyautogui
import telebot

from key import TOKEN, ID

bot = telebot.TeleBot(TOKEN)


def hi():
    bot.send_message(ID, "PON")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id,"Hi welcome sorry for using english keyboard if you don't understand it i just don't have another keyboard")
@bot.message_handler(commands=["screenshot"])
def start(message):
    from subprocess import call

    call(['screencapture', 'screenshot.jpg'])
    bot.send_document(1792342524,open("/Users/olhakhalimova/Documents/python/GItHub/1bot/screenshot.jpg","rb"))
@bot.message_handler(commands=["pin"])
def start(message):
    pin=["pin/photo_2024-05-07 16.43.11.jpeg","pin/photo_2024-05-07 16.43.17.jpeg","pin/photo_2024-05-07 16.43.27.jpeg","pin/photo_2024-05-07 16.43.32.jpeg"]
    bot.send_photo(message.from_user.id,open(random.choice(pin),"rb"), caption="pon")
@bot.message_handler(commands=["send"])
def start(message):
    import time
    # for i in range(20):
    #     time.sleep(2)
    #     bot.send_message(5277879764, "Я обещал")
    # text = message.text[5:]
    # grisha = 5277879764w
    # bot.send_message(grisha, text)
@bot.message_handler(content_types=["text"])
def start(message):
    user_text = message.text    # здесь сообщение юзера! его нужно обрабатывать
    user_id = message.from_user.id
    print(user_text, user_id)
    bot.send_dice(message.from_user.id,"⚽")
    bot.send_dice(message.from_user.id,"🎰")
    bot.send_dice(message.from_user.id,"🎳")


#hi()
bot.polling()
