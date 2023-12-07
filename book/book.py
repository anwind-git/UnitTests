class Book:
    def __init__(self, id, title=None, author=None):
        self.id = id
        self.title = title
        self.author = author

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author
