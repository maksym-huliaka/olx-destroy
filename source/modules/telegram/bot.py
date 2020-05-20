import sys
import traceback

import telegram
from telegram.ext import (Updater, CommandHandler, run_async)

from modules.publication_filter import get_current_time
from modules.states import get_bussy, set_bussy
from modules.telegram.bot_helper import send_publications, get_greeting, set_restriction_word, \
    get_urls, add_url, remove_url, run_url, get_url_greeting, send_test_message, throw_exception

BOT = telegram.Bot('1173914907:AAE0JaLYRR1VpWq-BJnOWzKNj89Qak3pSm0')


@run_async
def start_message(update, context):
    print(get_current_time() + " [OK][BOT] Catched message : " + update.message.text)
    context.bot.send_message(update.effective_chat.id,
                             get_greeting())


@run_async
def respawn_message(update, context):
    throw_exception(update.message, context.bot)


@run_async
def message_message(update, context):
    send_test_message(update.message, context.bot)


@run_async
def status_message(update, context):
    if not get_bussy():
        context.bot.send_message(update.effective_chat.id, "💤 I'm chilling. Ready for job.")
    else:
        context.bot.send_message(update.effective_chat.id, "👨🏻‍💻 I'm bussy. Go away, plz..")


@run_async
def url_message(update, context):
    print(get_current_time() + " [OK][BOT] Catched message : " + update.message.text)
    command = ""
    try:
        command = update.message.text.split()[1]
    except:
        context.bot.send_message(update.effective_chat.id, get_url_greeting())

    if command == '-add':
        try:
            add_url(update.message)
            context.bot.send_message(update.effective_chat.id,
                                     "✅OK!\nUrl is added to database. Now you can initialize it by \'-run\' tag")
        except:
            traceback.print_exc()
            context.bot.send_message(update.effective_chat.id, "❌ERROR!\nCan't add url")

    if command == '-remove':
        try:
            remove_url(update.message)
            context.bot.send_message(update.effective_chat.id, "✅OK!\nUrl is removed")
        except:
            traceback.print_exc()
            context.bot.send_message(update.effective_chat.id,
                                     "❌ERROR!\nUrl with such name not found! Or error is thrown!")

    if command == '-list':
        try:
            context.bot.send_message(update.effective_chat.id, "📋 List:")
            get_urls(update.effective_chat.id, BOT)
        except:
            traceback.print_exc()
            context.bot.send_message(update.effective_chat.id, "❌ERROR!\nError is thrown!")

    if command == '-run':
        try:
            run_url(update.message)
            context.bot.send_message(update.effective_chat.id, "✅OK!\nUrl is initialized")
        except:
            traceback.print_exc()
            context.bot.send_message(update.effective_chat.id,
                                     "❌ERROR!\nUrl with such name not found! Or error is thrown!")


@run_async
def word_message(update, context):
    print("[OK][BOT] Catched message : " + update.message.text)
    try:
        word = update.message.text.split()[1]
        category = update.message.text.split()[2]
        set_restriction_word(update.message)
        context.bot.send_message(update.effective_chat.id,
                                 "✅Success!\n New restriction word: \n\t       🔹 " + word + "\n Is added to category: \n\t       🔹 " + category)
    except:
        traceback.print_exc()
        context.bot.send_message(update.effective_chat.id,
                                 "⚠You can add new Restriction word ranges with that command in that style\n/word {word} {category} \n with valid word!")


@run_async
def pubs_message(update, context):
    print(get_current_time() + " [OK][BOT] Catched message : " + update.message.text)
    context.bot.send_message(update.effective_chat.id, '🕛 Wait a minute! Plz...')
    if not get_bussy():
        set_bussy(True)
        try:
            send_publications(update.effective_chat.id, context.bot)
        except:
            print(get_current_time()+" [ERROR] Publication getting method crashed with: ",sys.exc_info()[0])
        finally:
            set_bussy(False)
    else:
        context.bot.send_message(update.effective_chat.id, '✋🏻 Sorry.. in progress...')

    print(get_current_time() + " [OK][BOT] message sent")


def initialize_bot():
    # updater = Updater(token='1173914907:AAE0JaLYRR1VpWq-BJnOWzKNj89Qak3pSm0', use_context=True)
    updater = Updater(bot=BOT, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_message))
    dispatcher.add_handler(CommandHandler('pubs', pubs_message))
    dispatcher.add_handler(CommandHandler('word', word_message))
    dispatcher.add_handler(CommandHandler('url', url_message))
    dispatcher.add_handler(CommandHandler('status', status_message))
    dispatcher.add_handler(CommandHandler('message', message_message))
    dispatcher.add_handler(CommandHandler('respawn', respawn_message))
    updater.start_polling()
    updater.idle()
