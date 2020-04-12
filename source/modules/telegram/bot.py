import telebot

from modules.telegram.bot_helper import send_publications, get_greeting, set_price_range, set_restriction_word

BOT = telebot.TeleBot('1173914907:AAE0JaLYRR1VpWq-BJnOWzKNj89Qak3pSm0')

min_sum = '500'
max_sum = '1000'

keyboard1 = telebot.types.ReplyKeyboardMarkup()

keyboard1.row('/pubs')
keyboard1.row('/range', '/word')

@BOT.message_handler(commands=['start'])
def start_message(message):
    print("Catched message : "+ message.text)
    BOT.send_message(message.chat.id, get_greeting()
                     ,reply_markup=keyboard1)

@BOT.message_handler(commands=['range'])
def range_message(message):
    print("Catched message : "+ message.text)
    if set_price_range(message):
        BOT.send_message(message.chat.id, "Success! New price range added!")
    else:
        BOT.send_message(message.chat.id, "You can add new price ranges with that command in that style\n/range {min} {max}\n with valid numbers!")

@BOT.message_handler(commands=['word'])
def word_message(message):
    print("Catched message : "+ message.text)
    if set_restriction_word(message):
        BOT.send_message(message.chat.id, "Success! New restriction is added")
    else:
        BOT.send_message(message.chat.id, "You can add new Restriction word ranges with that command in that style\n/word {word} \n with valid word!")



@BOT.message_handler(content_types=['text'])
def send_text(message):
    print("Catched message : "+ message.text)
    if message.text == '/pubs' or message.text == 'Show Pubs':
        BOT.send_message(message.chat.id, 'Wait a minut plz')
        send_publications(message.chat.id, BOT)
    elif message.text == 'слава україні':
        BOT.send_message(message.chat.id, 'ГЕРОЯМ СЛАВА!')

