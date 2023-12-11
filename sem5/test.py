from contact_book import ContactBook
from contact import Contact
import unittest
from unittest.mock import patch
from io import StringIO


class TestContactBook(unittest.TestCase):

    def setUp(self):
        self.contact_book = ContactBook()

    def test_add_contact(self):
        """
        Тип: Модульный тест.
        Тест гарантирует, что контакт будет добавлен в книгу контактов и будет
        присутствовать в списке контактов.
        """
        contact = Contact("Иван Иванов", 123456, "email1@mail.ru")
        self.contact_book.add_contact(contact)
        self.assertIn(contact, self.contact_book.contacts)

    def test_edit_contact(self):
        """
        Тип: Модульный тест.
        Тест проверяет, что существующий контакт может быть успешно отредактирован.
        """
        old_contact = Contact("Иван Иванов", 123456, "email1@mail.ru")
        new_contact = Contact("Петр Петров", 123456, "email2@mail.ru")
        self.contact_book.add_contact(old_contact)
        self.assertTrue(self.contact_book.edit_contact("Иван Иванов", new_contact))
        self.assertIn(new_contact, self.contact_book.contacts)
        self.assertNotIn(old_contact, self.contact_book.contacts)

    def test_delete_contact(self):
        """
        Тип: Модульный тест.
        Тест проверяет, что контакт может быть удален из книги контактов.
        """
        contact = Contact("Иван Иванов", 123456, "email1@mail.ru")
        self.contact_book.add_contact(contact)
        self.assertTrue(self.contact_book.delete_contact("Иван Иванов"))
        self.assertNotIn(contact, self.contact_book.contacts)

    def test_display_contacts(self):
        """
        Тип: Модульный тест.
        Тест гарантирует, что контакты будут правильно отображаться при вызове метода display_contacts.
        """
        contact = Contact("Иван Иванов", 123456, "email1@mail.ru")
        self.contact_book.add_contact(contact)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_book.display_contacts()
            self.assertEqual(mock_stdout.getvalue().strip(), str(contact))

    def test_integration_add_and_display(self):
        """
        Тип: Интеграционный тест.
        Тест проверяет, приводит ли добавление контакта и последующее отображение контактов к ожидаемому результату.
        Ожидаемым выходным сигналом является строковое представление контакта, а фактический вывод фиксируется с
        помощью объекта. Если захваченные выходные данные совпадают с ожидаемой строкой, тест будет пройден.
        """
        contact = Contact("Иван Иванов", 123456, "email1@mail.ru")
        self.contact_book.add_contact(contact)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_book.display_contacts()
            self.assertEqual(mock_stdout.getvalue().strip(), str(contact))

    def test_integration_edit_and_display(self):
        """
        Тип: Интеграционный тест.
        Тестирует интеграцию редактирования контакта в книге контактов и отображения контактов. Он проверяет, что
        редактирование контакта и совместное отображение контактов дают ожидаемый результат.
        """
        old_contact = Contact("Иван Иванов", 123456, "email1@mail.ru")
        new_contact = Contact("Петр Петров", 123456, "email2@mail.ru")
        self.contact_book.add_contact(old_contact)
        self.contact_book.edit_contact("Иван Иванов", new_contact)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_book.display_contacts()
            expected_output = f"{new_contact}"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_end_to_end_scenario(self):
        """
        Сквозное тестирование.
        Тестирует комплексный сценарий, включающий несколько операций, добавление, редактирование и удаление
        контактов. Проверяет ожидаемое поведение при последовательном выполнении нескольких операций.
        """
        contact1 = Contact("Иван Иванов", 123456, "email1@mail.ru")
        contact2 = Contact("Иван Иванов", 123456, "email1@mail.ru")

        self.contact_book.add_contact(contact1)
        self.contact_book.add_contact(contact2)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_book.display_contacts()
            expected_output = f"{contact1}\n{contact2}"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

        self.assertTrue(self.contact_book.edit_contact("Иван Иванов", Contact("Петр Петров", 123456, "email2@mail.ru")))

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_book.display_contacts()
            expected_output = f"{Contact('Петр Петров', 123456, 'email2@mail.ru')}\n{contact2}"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

        self.assertTrue(self.contact_book.delete_contact("Иван Иванов"))

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_book.display_contacts()
            expected_output = f"{Contact('Петр Петров', 123456, 'email2@mail.ru')}"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
