""""
1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
    Примечание: Списки фруктов создайте вручную в начале файла.
2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим
условиям:
Элемент кратен 3,
Элемент положительный,
Элемент не кратен 4.

Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
10-20 чисел в списке вполне достаточно.
3. Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список из квадратных корней
чисел (если число положительное) и самих чисел (если число отрицательное) и возвращает результат (желательно применить
генератор и тернарный оператор при необходимости). В результате работы функции исходный список не должен измениться.
Например:
old_list = [1, -3, 4]
result = [1, -3, 2]

    Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
    10-20 чисел в списке вполне достаточно.
4. Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13, функция поднимает исключительную
ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
Далее написать основной код программы. Пользователь вводит число. Введенное число передаем параметром в написанную
функцию и печатаем результат, который вернула функция. Обработать возможность возникновения исключительной ситуации,
которая поднимается внутри функции.
"""

import math
import random

rand_list = [random.randint(-50, 50) for i in range(20)]
print(rand_list)
#
# num = 1 if rand_list else 2
# print(num)
#
# result = rand_list or [None]
# print(result)
#
# result = rand_list or [] or [0]
# print(result)
#
# result = rand_list and [] and [0]
# print(result)
#
# a_list = [1, 2, [1, 2]]
# print(a_list)
# b_list = a_list.copy()
# b_list[2][1] = 200
# print(b_list)
# result = copy.deepcopy(b_list)
# result[2][1] = 300
# print(b_list)
# print(result)


man = ['яблоко', "апельсин", "груша"]
woman = ['яблоко', 'киви', 'манго', 'арбуз', 'груша']
result = [el for el in man if el in woman]
print(result)

numbers = [num for num in rand_list if num > 0 and num % 3 == 0 and num % 4 != 0]
print(numbers)


def get_list(list):
    list_copy = list.copy()
    result = [int(math.sqrt(el)) if el > 0 else el for el in list_copy]
    print(result)


get_list(rand_list)


def get_except():
    rand_list = [random.randint(1, 100) for i in range(20)]
    print(rand_list)
    result = []
    for el in rand_list:
        try:
            if el == 13:
                raise Exception('Число тринадцать!')
            else:
                result.append(el)
        except Exception as e:
            print(e)
    return result


print(get_except())