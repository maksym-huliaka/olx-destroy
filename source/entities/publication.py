class Publication:
    def __init__(self, link, title, description):
        self.link = link
        self.title = title
        self.description = description
    
    def print(self):
        print(self.title)
        print(self.description)
        print(self.link + '\n')