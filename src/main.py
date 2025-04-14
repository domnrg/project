"""Написать функцию, которая получает на вход список чисел и
возвращает новый список, содержащий только числа, которые являются палиндромами.

Пример ввода:
[121, 123, 131, 34543]

Пример вывода:
[121, 131, 34543]"""

from typing import List


def get_polindrom_numbers(number_list: List[int]) -> List[int]:
    """Функция для получения списка полиндромов"""

    polindrom_list = []

    for num in number_list:
        if str(num) == str(num)[::-1]:
            polindrom_list.append(num)

    return polindrom_list


if __name__ == "__main__":
    print(get_polindrom_numbers([121, 123, 131, 34543]))
