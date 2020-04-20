import codecs
import time

from entities.url import Url
from modules.database.repository.impl import url_repository, word_repository
from modules.olx_handler import get_publications
from modules.path import FILE_GREETING_PATH, FILE_WORDS_PATHS, FILE_URL_GREETING_PATH

url = None


def get_urls(chatid, BOT):
    url_message = ''
    urls = url_repository.get()
    for url in urls:
        url_message = url_message + url.to_string()
    BOT.send_message(chatid, url_message)


def add_url(message):
    url_name = message.text.split()[2]
    url_category = message.text.split()[3]
    url_link = message.text.split()[4]
    url = Url(url_link, url_name, url_category)
    url_repository.save(url)


def remove_url(message):
    url_name = message.text.split()[2]
    url_repository.delete(url_name)


def run_url(message):
    url_name = message.text.split()[2]
    global url
    url = url_repository.get_by_name(url_name)


def send_publications(chatid, BOT):
    global url
    if url is None:
        BOT.send_message(chatid, "WARNING! Uninitialized url")
    else:
        salo = get_publications(url)
        for pub in salo:
            BOT.send_message(chatid, pub.to_string())
            time.sleep(3)


def get_greeting():
    return open(FILE_GREETING_PATH).read()


def get_url_greeting():
    return open(FILE_URL_GREETING_PATH).read()


def set_restriction_word(message):
        word = message.text.split()[1]
        category = message.text.split()[2]
        print(word+" ["+category+"]")
        word_repository.save(word,category)


def send_test_message(chatid, BOT):
    BOT.send_message(chatid, "test message@")
