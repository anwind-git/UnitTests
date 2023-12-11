from contact_book import ContactBook
from contact import Contact


def main():
    address_book = ContactBook()

    while True:
        print("\n1. Добавить контакт\n2. Редактировать контакт\n3. Удалить контакт\n4. Все контакты\n5. Выход")
        choice = input("Enter: ")

        if choice == "1":
            name = input("Имя: ")
            phone_number = input("Телефон: ")
            email = input("Электронная почта: ")
            new_contact = Contact(name, phone_number, email)
            address_book.add_contact(new_contact)
            print("Контакт успешно добавлен.")

        elif choice == "2":
            old_name = input("Введите имя контакта для редактирования: ")
            new_name = input("Введите новое имя: ")
            new_phone_number = input("Введите новый номер телефона: ")
            new_email = input("Введите новый адрес электронной почты: ")
            edited_contact = Contact(new_name, new_phone_number, new_email)
            if address_book.edit_contact(old_name, edited_contact):
                print("Контакт успешно отредактирован")
            else:
                print("Контакт не найден.")

        elif choice == "3":
            name_to_delete = input("Введите имя контакта, который нужно удалить: ")
            if address_book.delete_contact(name_to_delete):
                print("Контакт успешно удален")
            else:
                print("Контакт не найден.")

        elif choice == "4":
            address_book.display_contacts()

        elif choice == "5":
            break

        else:
            print("Ошибка. Пожалуйста, повторите снова.")


if __name__ == "__main__":
    main()
