"""
Задание 5
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

new_list = [el for el in range(100, 1001) if el % 2 == 0]
print(len(new_list))  # Для наглядности
sum_list = reduce(lambda x, y: x + y, new_list)  # В соответствии с условиями задания
sum_list_summa = sum(new_list)  # Короткий вариант
print('Сгенерированный список: \n', new_list)
print('Сумма значений перый вариант: \n', sum_list)
print('Сумма значений: второй вриант\n', sum_list_summa)
