from in_memory_book_repository import InMemoryBookRepository
from book_service import BookService

book_repository = InMemoryBookRepository()

book_service = BookService(book_repository)

book_id = "1"
book = book_service.find_book_by_id(book_id)
print(f"Книга найдена: {book.get_title()} автор: {book.get_author()}")

books = book_service.find_all_books()
print("Все книги:")
for book in books:
    print(f"- {book.get_title()} автор: {book.get_author()}")
