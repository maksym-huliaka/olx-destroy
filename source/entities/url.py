class Url:
    def __init__(self, url, name, category):
        self.url = url
        self.name = name
        self.category = category

    def to_string(self):
        return self.name + ' [' +self.category + ']\n' + self.url + '\n\n'
