import traceback

import telebot

from modules.publication_filter import get_current_time
from modules.states import bussy, get_bussy, set_bussy
from modules.telegram.bot_helper import send_publications, get_greeting, set_restriction_word, \
    get_urls, add_url, remove_url, run_url, get_url_greeting, send_test_message, throw_exception

BOT = telebot.TeleBot('1173914907:AAE0JaLYRR1VpWq-BJnOWzKNj89Qak3pSm0')

keyboard1 = telebot.types.ReplyKeyboardMarkup()

keyboard1.row('/pubs')
keyboard1.row('/url', '/word')


@BOT.message_handler(commands=['start'])
def start_message(message):
    print(get_current_time()+" [OK][BOT] Catched message : " + message.text)
    BOT.send_message(message.chat.id,
                     get_greeting(),
                     reply_markup=keyboard1)

@BOT.message_handler(commands=['respawn'])
def start_message(message):
    throw_exception(message, BOT)

@BOT.message_handler(commands=['message'])
def start_message(message):
    send_test_message(message, BOT)

@BOT.message_handler(commands=['status'])
def start_message(message):
    if not get_bussy():
        BOT.send_message(message.chat.id, "💤 I'm chilling. Ready for job.")
    else:
        BOT.send_message(message.chat.id, "👨🏻‍💻 I'm bussy. Go away, plz..")

@BOT.message_handler(commands=['url'])
def url_message(message):
    print(get_current_time()+" [OK][BOT] Catched message : " + message.text)
    command = ""
    try:
        command = message.text.split()[1]
    except:
        BOT.send_message(message.chat.id, get_url_greeting())

    if command == '-add':
        try:
            add_url(message)
            BOT.send_message(message.chat.id, "✅OK!\nUrl is added to database. Now you can initialize it by \'-run\' tag")
        except:
            traceback.print_exc()
            BOT.send_message(message.chat.id, "❌ERROR!\nCan't add url")

    if command == '-remove':
        try:
            remove_url(message)
            BOT.send_message(message.chat.id, "✅OK!\nUrl is removed")
        except:
            traceback.print_exc()
            BOT.send_message(message.chat.id, "❌ERROR!\nUrl with such name not found! Or error is thrown!")

    if command == '-list':
        try:
            BOT.send_message(message.chat.id, "📋 List:")
            get_urls(message.chat.id, BOT)
        except:
            traceback.print_exc()
            BOT.send_message(message.chat.id, "❌ERROR!\nError is thrown!")

    if command == '-run':
        try:
            run_url(message)
            BOT.send_message(message.chat.id, "✅OK!\nUrl is initialized")
        except:
            traceback.print_exc()
            BOT.send_message(message.chat.id, "❌ERROR!\nUrl with such name not found! Or error is thrown!")


@BOT.message_handler(commands=['word'])
def word_message(message):
    print("[OK][BOT] Catched message : " + message.text)
    try:
        word = message.text.split()[1]
        category = message.text.split()[2]
        set_restriction_word(message)
        BOT.send_message(message.chat.id,
                         "✅Success!\n New restriction word: \n\t       🔹 " + word + "\n Is added to category: \n\t       🔹 " + category)
    except:
        traceback.print_exc()
        BOT.send_message(message.chat.id,
                         "⚠You can add new Restriction word ranges with that command in that style\n/word {word} {category} \n with valid word!")

@BOT.message_handler(commands=['pubs'])
def pubs_message(message):
    print(get_current_time()+" [OK][BOT] Catched message : " + message.text)
    BOT.send_message(message.chat.id, '🕛 Wait a minute! Plz...')
    if not get_bussy():
        set_bussy(True)
        send_publications(message.chat.id, BOT)
        set_bussy(False)
    else:
        BOT.send_message(message.chat.id, '✋🏻 Sorry.. in progress...')

    print(get_current_time()+" [OK][BOT] message sent")
