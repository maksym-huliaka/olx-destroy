import traceback

import telebot

from modules.telegram.bot_helper import send_publications, get_greeting, set_restriction_word, \
    get_urls, add_url, remove_url, run_url, get_url_greeting

BOT = telebot.TeleBot('1173914907:AAE0JaLYRR1VpWq-BJnOWzKNj89Qak3pSm0')

min_sum = '500'
max_sum = '1000'

keyboard1 = telebot.types.ReplyKeyboardMarkup()

keyboard1.row('/pubs')
keyboard1.row('/url', '/word')


@BOT.message_handler(commands=['start'])
def start_message(message):
    print("Catched message : " + message.text)
    BOT.send_message(message.chat.id,
                     get_greeting(),
                     reply_markup=keyboard1)


@BOT.message_handler(commands=['url'])
def url_message(message):
    command = ""
    try:
        command = message.text.split()[1]
    except:
        BOT.send_message(message.chat.id, get_url_greeting())

    if command == '-add':
        try:
            add_url(message)
            BOT.send_message(message.chat.id, "OK! Url is added to database. Now you can initialize it by \'-run\' tag")
        except:
            traceback.print_exc()
            BOT.send_message(message.chat.id, "ERROR! Cant add url")

    if command == '-remove':
        try:
            remove_url(message)
            BOT.send_message(message.chat.id, "OK! Url is removed")
        except:
            traceback.print_exc()
            BOT.send_message(message.chat.id, "ERROR! Url with such name not found! Or error is thrown!")

    if command == '-list':
        try:
            get_urls(message.chat.id, BOT)
        except:
            traceback.print_exc()
            BOT.send_message(message.chat.id, "ERROR! Error is thrown!")

    if command == '-run':
        try:
            run_url(message)
            BOT.send_message(message.chat.id, "OK! Url is initialized")
        except:
            traceback.print_exc()
            BOT.send_message(message.chat.id, "ERROR! Url with such name not found! Or error is thrown!")


@BOT.message_handler(commands=['word'])
def word_message(message):
    print("Catched message : " + message.text)
    try:
        word = message.text.split()[1]
        category = message.text.split()[2]
        set_restriction_word(message)
        BOT.send_message(message.chat.id,
                         "Success! New restriction word: '" + word + "' is addedto category :" + category)
    except:
        traceback.print_exc()
        BOT.send_message(message.chat.id,
                         "You can add new Restriction word ranges with that command in that style\n/word {word} {category} \n with valid word!")


@BOT.message_handler(content_types=['text'])
def send_text(message):
    print("Catched message : " + message.text)
    if message.text == '/pubs' or message.text == 'Show Pubs':
        BOT.send_message(message.chat.id, 'Wait a minut plz')
        send_publications(message.chat.id, BOT)
    elif message.text == 'слава україні':
        BOT.send_message(message.chat.id, 'ГЕРОЯМ СЛАВА!')
