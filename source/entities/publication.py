class Publication:
    def __init__(self, link, title, description, price):
        self.price = price
        self.link = link
        self.title = title
        self.description = description
    
    def print(self):
        print(self.title)
        print(self.price)
        print(self.link)
        print(self.description + '\n')
