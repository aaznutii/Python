"""
Задание 6
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
import random
import itertools

begin_val = int(input('Укажите с какого числа  начать генерацию чисел?\n'))
final_val = int(input('Укажите до какого числа генерировать список?\n'))
new_list = [el for el in range(begin_val, final_val)]
# new_list = [itertools.cycle(range(begin_val, final_val))]
print(new_list)
# repeat_list = [itertools.cycle(new_list) if itertools.count()]
# print(repeat_list)
с = 0
for el in itertools.cycle(new_list):
    if с > 10:
        break
    print(el)
    с += 1
