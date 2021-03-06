import time

from entities.url import Url
from modules.database.repository.impl import url_repository, word_repository, default_url_repository
from modules.olx_handler import get_publications
from modules.util.config import config

url = None
chatid1 = None

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
    default_url_repository.update(url)


def send_publications(chatid, BOT):
    global chatid1
    chatid1 = chatid
    global url
    if url is None:
        BOT.send_message(chatid, "🌏 Initializing URL..")
        url = default_url_repository.get()
        print(url)
    BOT.send_message(chatid, "🔐 Accessing web-pages..")
    salo = get_publications(url, chatid, BOT)
    if not salo:
        BOT.send_message(chatid, "😥 There are no new publications.")
        return
    BOT.send_message(chatid, "☝ There are all publications for now.")

def get_greeting():
    return "🙋 Hello, my Friend, wanna  show u some things? \n\nYou can use that commands:\n🌏 To add new URL ya want to search pubs: /url\n📢 To show pubs: /pubs\n📛 To add restriction word: /word {ur word} {category}\n\nGut Luk(pognali) ♿"


def get_url_greeting():
    return "🙋 Hello again, ya can fully customize your URLs\n\n" +"Use such commands:\n" +"📋 To show URLs:\n" +"           ☀/url -list\n" +"➕ To add new URL:\n" +"           ☀/url -add {name} {category} {link}\n" +"➖ To remove URL:\n" +"           ☀/url -remove {name}\n" +"🌏 To choose running URL ya want to see publications:\n" +"           ☀/url -run {name}\n\n" +"Gut Luk again 😏"


def set_restriction_word(message):
        word = message.text.split()[1]
        category = message.text.split()[2]
        print(word+" ["+category+"]")
        word_repository.save(word,category)


def throw_exception(message, BOT):
    text = " ".join(message.text.split()[1:])
    print(text)
    BOT.send_message(config().get("telegram.chat_id"), text)

def send_test_message(message, BOT):
    try:
        text = " ".join(message.text.split()[1:])
        print(text)
        BOT.send_message(config().get("telegram.chat_id"), text)
    except:
        a="do nothing"
