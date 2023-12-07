class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def find_book_by_id(self, id):
        return self.book_repository.find_by_id(id)

    def find_all_books(self):
        return self.book_repository.find_all()
