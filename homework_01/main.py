"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def simple_number(number):
    attemp = 0
    if number  > 1:
        for i in range(1, number + 1):
            if number % i == 0:
                attemp += 1
        if attemp <= 2:
            return number


def is_prine(number):
    if simple_number(number):
        return True


def odd_number(num):
    if num % 2 != 0:
        return True


def even_number(num):
    if num % 2 == 0:
        return True


def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(odd_number, numbers_list))
    if filter_type == EVEN:
        return list(filter(even_number, numbers_list))
    if filter_type == PRIME:
        return list(filter(is_prine, numbers_list))


def main():
    print(power_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    print(filter_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], ODD))
    print(filter_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], EVEN))
    print(filter_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11], PRIME))


if __name__=="__main__":
    main()
