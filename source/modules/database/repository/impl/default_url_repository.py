from modules.database.repository import repository


def update(url):
    repository.delete_all("default_url")
    repository.save("default_url", ["url"], [url.url])

def get():
    return repository.get("default_url", ["url"])[0][0]
