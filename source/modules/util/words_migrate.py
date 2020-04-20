import codecs

from modules.database.repository.impl import word_repository
FILE_WORDS_PATHS = "/app/source/resources/words.ini"

def migrate_to_db():
    file = codecs.open(FILE_WORDS_PATHS, 'r', 'utf_8_sig')
    words = file.readlines()
    file.close()
    for word in words:
        good_word = word[:-2]
        word_repository.save(good_word,"bich_nouts")
