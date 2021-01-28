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
import itertools


def get_new_list():  # Первый итератор в форме обычной функции
    begin_val = int(input('Укажите с какого числа  начать генерацию чисел?\n'))
    final_val = int(input('Укажите до какого числа включительно генерировать список?\n'))
    new_list = []
    for el in itertools.count(begin_val):
        if el <= final_val:
            new_list.append(el)
        else:
            break
    return new_list


def repeat_list():  # Второй итератор в форме обычной функции
    new_list = get_new_list()
    rep_list = []
    count_repeat = int(input('Укажите количество повторений')) * len(new_list)
    count = 0
    for el in itertools.cycle(new_list):
        if count <= count_repeat:
            rep_list.append(el)
            count += 1
        else:
            break
    print(rep_list)


# более просой пособ для первого итератора пока не придумал.


def repeat_list_simple():  # Простой способ повторения
    new_list = [el for el in itertools.repeat(get_new_list(), int(input('Укажите количество повторений\n')))]
    print(new_list)

# repeat_list_simple()
