class Publication:
    def __init__(self, link, title, description, price):
        self.price = price
        self.link = link
        self.title = title
        self.description = description
    
    def to_string(self):
        return self.title+'\n'+'Price: '+self.price+'\n\n'+self.description +'\n\nLink: '+self.link+'\n'

