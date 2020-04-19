from modules.database.repository import repository


def update(new_time, url_name):
    repository.delete("tme", "url_name", url_name)
    repository.save("tme", ["tme", "url_name"], [new_time, url_name])


def get(url_name):
    return repository.get_by("tme", ["tme"], "url_name", url_name)[0][0]




