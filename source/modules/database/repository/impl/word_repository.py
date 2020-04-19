from modules.database.repository import repository


def save(word, category):
    repository.save("words", ["word","category"], [word,category])

def get(category):
    return repository.get_by("words", ["word"],"category", category)

def delete(word):
    repository.delete("words", "word",word)
