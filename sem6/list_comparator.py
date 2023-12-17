"""
Этот модуль сравнивает два списка и определяет какой список, имеет большее среднее значение.
"""


class ListComparator:
    """
    Этот класс сравнивает два списка и определяет, какой из них имеет большее среднее значение.
    """

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        """
        Вычисляет среднее значение для заданного списка.
        """
        return sum(lst) / len(lst)

    def compare_lists(self):
        """
        Сравнивает средние значения списков list1 и list2 и возвращает результат.
        """
        average1 = self.calculate_average(self.list1)
        average2 = self.calculate_average(self.list2)
        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        return (
            "Второй список имеет большее среднее значение"
            if average1 < average2
            else "Средние значения равны"
        )
