from entities.url import Url
from modules.database.repository import repository


def update(url):
    repository.delete_all("default_url")
    repository.save("default_url", ["url","name", "category"], [url.url, url.name, url.category])

def get():
    result_map = repository.get("default_url", ["url","name","category"])
    urls=[]
    for obj in result_map:
        url = Url(obj[0],obj[1], obj[2])
        urls.append(url)
    return urls[0]
