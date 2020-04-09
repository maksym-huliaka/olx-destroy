import codecs
import re
from datetime import datetime

TIME_PATTERN = "([01]?[0-9]|2[0-3]):[0-5][0-9]"
TODAY_PATTERN = "Сегодня"
FILE_LAST_UPDATE_TIME_PATH = "resources/time.ini"
FILE_WORDS_PATHS = "resources/words.ini"


def filter_by_time(publications):
    last_update_time = get_last_update_time()
    time_succesfull_pubs = []
    for pub in publications:
        pub_time = get_date(pub.text)

        if pub_time is not False and pub_time > last_update_time:
            time_succesfull_pubs.append(pub)
        break
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
    except:
        return False
    return datetime.strptime(result, '%H:%M')


def get_last_update_time():
    time_text = open(FILE_LAST_UPDATE_TIME_PATH).read()
    return datetime.strptime(time_text, '%H:%M')


def save_current_time():
    current_time = datetime.now().strftime("%H:%M")
    text_file = open(FILE_LAST_UPDATE_TIME_PATH, 'w')
    text_file.write(current_time)
    text_file.close()
