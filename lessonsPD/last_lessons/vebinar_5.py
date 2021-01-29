import functools
import itertools
#
# a = list(map(str, [1, 2, 3, 4, 5])) # применяет функцию к итерируемому объекту
# print(a)
#
# b = functools.reduce(lambda acc, x: acc*x, [1, 2, 3])
# print(b)
#
# d= functools.reduce(lambda acc, x: (acc[1], acc[0] + acc[1]), [1, 2, 3], (1, 1))
# print(d)
#
#
# def reverse(acc, x):
#     return x + acc
#
#
# s = functools.reduce(reverse, 'asdfgs')
# print(s)
#
#
# def power(x, y):
#     return x**y
#
# # l = list(map(power, [1, 2, 3, 4, 5]))
#
#
# # Возврат с частично заполенными значениями
# square = functools.partial(power, y=2)
# res = square(3)
# print(res)
#
# def exper(x, y):
#     return x + y(x)
#
#
# e2 = functools.partial(exper, y=int(input()))
#
#
# summ = list(map(sum, [(1, 2), (5, 9)]))
# print(summ)
#
#
# def gen(x):
#     for y in range(1, x+1):
#         yield y * y


# def repit_new():
#     j = 1
#     for i in itertools.repeat({}, 10):
#         i[j] = j
#         j += 1
#         print(i)
#
#
# repit_new()


# cy = list(itertools.chain(range(5), range(5,0, -1))) # соединяет генераторы
# print(cy)
#
# print(list(itertools.chain('fhfhfh', "jgjg", 'jgjfjh', {1, 2, 3, 4})))

# отбор ложных выражений
# print(list(itertools.filterfalse(lambda x: x == 3, range(20))))
