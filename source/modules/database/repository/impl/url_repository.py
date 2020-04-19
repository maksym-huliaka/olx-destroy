from entities.url import Url
from modules.database.repository import repository

def save(url):
    repository.save("urls", ["url","name", "category"], [url.url, url.name, url.category])
    repository.save("tme", ["tme", "url_name"], ["04-14 00:00", url.name])

def get():
    result_map = repository.get("urls", ["url","name","category"])
    urls=[]
    for obj in result_map:
        url = Url(obj[0],obj[1], obj[2])
        urls.append(url)
    return urls

def get_by_name(name):
    result_map = repository.get_by("urls", ["url","name","category"], "name", name)
    urls=[]
    for obj in result_map:
        url = Url(obj[0],obj[1], obj[2])
        urls.append(url)
    return urls[0]

def delete(word):
    repository.delete("urls", "name",word)
