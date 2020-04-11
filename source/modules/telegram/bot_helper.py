import codecs
import time
from modules.olx_handler import get_publications
from modules.publication_filter import FILE_WORDS_PATHS

FILE_GREETING_PATH='/app/source/resources/greeting.ini'
FILE_PRICE_RANGE_PATH='/app/source/resources/price_range.ini'

def get_price(n):
    return open(FILE_PRICE_RANGE_PATH).readlines()[n]

def set_price_range(message):
    try:
        min=message.text.split()[1]
        max=message.text.split()[2]
    except:
        return False

    try:
        if(int(min)>int(max)):
            return False
    except:
        return False
    try:
        open(FILE_PRICE_RANGE_PATH,"w").write(min+"\n"+max)
        return True
    except:
        return False

def send_publications(chatid, BOT):
    salo = get_publications(get_price(0), get_price(1))
    for pub in salo:
        BOT.send_message(chatid, pub.to_string())
        time.sleep(1)

def get_greeting():
    return open(FILE_GREETING_PATH).read()

def set_restriction_word(message):
    try:
        word=message.text.split()[1]
        print(word)
        codecs.open(FILE_WORDS_PATHS, "a", "utf-8").write(word+"\n")
        return True
    except:
        return False

def send_test_message(chatid, BOT):
        BOT.send_message(chatid, "test message@")
