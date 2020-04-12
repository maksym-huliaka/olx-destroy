import codecs
import re
from datetime import datetime

from modules.path import FILE_WORDS_PATHS, FILE_LAST_UPDATE_TIME_PATH

TIME_PATTERN = "([01]?[0-9]|2[0-3]):[0-5][0-9]"
TODAY_PATTERN = "Сегодня"


def filter_by_time(publications):

    time_succesfull_pubs = []
    last_update_time = get_last_update_time()
    for pub in publications:
        pub_time = get_date(pub.text)
        if pub_time is not False and pub_time > last_update_time:
            time_succesfull_pubs.append(pub)
    save_current_time()
    return time_succesfull_pubs


def filter_by_words(text):
    text = text.lower()
    file = codecs.open(FILE_WORDS_PATHS, 'r', 'utf_8_sig')
    words = file.readlines()
    file.close()

    for word in words:
        good_word = word[:-2]
        if good_word in text:
            return False
    return True


def get_date(text):
    try:
        re.search(TODAY_PATTERN, text).group(0)
        result = re.search(TIME_PATTERN, text).group(0)
        result = datetime.now().strftime("%m-%d ")+result
    except:
        return False
    return datetime.strptime(result, '%m-%d %H:%M')


def get_last_update_time():
    time_text = open(FILE_LAST_UPDATE_TIME_PATH).read()
    return datetime.strptime(time_text, '%m-%d %H:%M')


def save_current_time():
    current_time = datetime.now().strftime("%m-%d %H:%M")
    text_file = open(FILE_LAST_UPDATE_TIME_PATH, 'w')
    text_file.write(current_time)
    text_file.close()
