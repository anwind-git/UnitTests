import unittest
from unittest.mock import MagicMock
from book import Book
from book_service import BookService


class BookServiceTestCase(unittest.TestCase):
    def test_find_book_by_id(self):
        # Создаем мок-объект BookRepository
        book_repository_mock = MagicMock()

        # Устанавливаем ожидаемое значение для метода find_by_id
        book_id = "1"
        expected_book = Book(book_id, "Book1", "Author1")
        book_repository_mock.find_by_id.return_value = expected_book

        # Создаем экземпляр BookService с мок-объектом BookRepository
        book_service = BookService(book_repository_mock)

        # Вызываем метод find_book_by_id
        actual_book = book_service.find_book_by_id(book_id)

        # Проверяем, что метод find_by_id был вызван с правильным аргументом
        book_repository_mock.find_by_id.assert_called_once_with(book_id)

        # Проверяем, что возвращенная книга соответствует ожидаемой
        self.assertEqual(actual_book, expected_book)

    def test_find_all_books(self):
        # Создаем мок-объект BookRepository
        book_repository_mock = MagicMock()

        # Устанавливаем ожидаемое значение для метода find_all
        expected_books = [
            Book("1", "Book1", "Author1"),
            Book("2", "Book2", "Author2")
        ]
        book_repository_mock.find_all.return_value = expected_books

        # Создаем экземпляр BookService с мок-объектом BookRepository
        book_service = BookService(book_repository_mock)

        # Вызываем метод find_all_books
        actual_books = book_service.find_all_books()

        # Проверяем, что метод find_all был вызван
        book_repository_mock.find_all.assert_called_once()

        # Проверяем, что возвращенный список книг соответствует ожидаемому
        self.assertEqual(actual_books, expected_books)


if __name__ == "__main__":
    unittest.main()
