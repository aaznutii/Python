"""
Задание 2
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

import random


def get_random_list():
    """
    Генерация списка на основе данных пользователя и выборка заданного количества случайных чисел
    :return: list[choices int]
    """
    for_max_list = input('Укажите максимальное значение исходного списка\n')
    len_list = input('Укажите длинну исходного списка\n')
    new_list = random.choices([el for el in range(int(for_max_list))], k=int(len_list))
    return new_list


# get_random_list()
def choices_numbers():
    """
    Вывод элементов исходного списка, значения которых больше предыдущего элемента.
    Решено как генерация списка с выборкой по условию.
    :return: list
    """
    first_list = get_random_list()
    print('Искодный список:\n', first_list)
    final_list = [el for i, el in enumerate(first_list) if el > first_list[i - 1] and i != 0]
    print('Итоговый список', final_list)


# choices_numbers()
