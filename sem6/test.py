import pytest
from list_comparator import ListComparator


def test_first_list_is_bigger():
    list1 = [6, 7, 8, 9, 10]
    list2 = [1, 2, 3, 4, 5]
    comparator = ListComparator(list1, list2)
    result = comparator.compare_lists()
    assert result == "Первый список имеет большее среднее значение"


def test_second_list_is_bigger():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    comparator = ListComparator(list1, list2)
    result = comparator.compare_lists()
    assert result == "Второй список имеет большее среднее значение"


def test_lists_are_equal():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    comparator = ListComparator(list1, list2)
    result = comparator.compare_lists()
    assert result == "Средние значения равны"


if __name__ == "__main__":
    pytest.main()
