def get_list(*args):
    el = args
    print(args)
    print(el)


num = [2, 5, 'ghgh']
get_list(2, 5, 'ghgh', num)


def print_list(**kwargs):
    for name, el in kwargs.items():
        print(el)


print_list(name=5, count=10)

# сортировка
sity2 = (('Moskv', 5000), ('Samara', 2000), ('Revo', 1000))
print(sorted(sity2))
print(sorted(sity2, key=lambda x: x[1]))

# Особый объект - фильтр. Функция рабтает с любыми итерируемыми объектами.
names = ['Kate', 'Max', 'Alex']
print(filter(lambda x: len(x) > 3, names))
print(list(filter(lambda x: len(x) > 3, names)))

# мфп
n = [1, 2, 3, 4]
print(list(map(lambda x: x * x, n)))

import os
import sys

name = sys.platform
for i in range(1, 5):
    new_dir = os.path.join(os.getcwd(), f'{name}_{i}')
    os.mkdir(new_dir)
