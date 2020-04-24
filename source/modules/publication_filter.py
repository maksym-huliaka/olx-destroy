import re
from datetime import datetime

import pytz

from modules.database.repository.impl import time_repository

TIME_PATTERN = "([01]?[0-9]|2[0-3]):[0-5][0-9]"
TODAY_PATTERN = "Сегодня"


def filter_by_time(publications, url):

    time_succesfull_pubs = []
    last_update_time = get_last_update_time(url)
    for pub in publications:
        pub_time = get_date(pub.text)
        if pub_time is not False and pub_time > last_update_time:
            time_succesfull_pubs.append(pub)
    return time_succesfull_pubs


def filter_by_words(text, words):
    text = text.lower()
    for word in words:
        good_word = word[0]
        if good_word in text:
            return False
    return True


def get_date(text):
    try:
        re.search(TODAY_PATTERN, text).group(0)
        result = re.search(TIME_PATTERN, text).group(0)
        result = datetime.now().strftime("%m-%d")+result
    except:
        return False
    return datetime.strptime(result, '%m-%d %H:%M')


def get_last_update_time(url):
    repo_time = time_repository.get(url.name)
    time = datetime.strptime(repo_time, '%m-%d %H:%M')
    return time


def save_current_time(url):
    time_repository.update(get_current_time(), url.name)

def get_current_time():
    return datetime.now().strftime("%m-%d %H:%M")
