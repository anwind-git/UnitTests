class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Имя: {self.name}, Телефон: {self.phone_number}, Электронная почта: {self.email}"
