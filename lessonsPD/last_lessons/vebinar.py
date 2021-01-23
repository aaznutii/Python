import keyword

# print(keyword.kwlist)
# print(len(keyword.kwlist))
#
# for el in keyword.kwlist:
#     print(el)

"""
36
False
None
True
__peg_parser__
and
as
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield
"""
# a = None
# while a is None:
#     try:
#         a = int(input('Введите число'))
#     except ValueError:
#         print('Вы ввели не число')
#     except IndexError:
#         print('Далеко зашли')
#     else:
#         print("ок")
#     # except Exception as e:
#     #     print("Перехватывает почти Все исключения - плохая практика", str(e))
#     finally:
#         print('То, что будет сделано в любом случае')


# def city_data():
#     hous = int(input('дома'))
#     temper = int(input('temp'))
#     return hous, temper
#
#
# def calc_temp():
#     hous, temp = city_data()
#     e = 2 * (temp * 10) * hous
#     print(e)


e = [1, 2, 2, 3]
f = e.copy()


def f(num, b=None):
    if b is None:
        b = []
    b = num
    print(b, 'в значениях по умолчанию не использовать сложные объекты')


d = [1, 2, 3, 4, 5, 6, 7]


def my_sort(value):
    global a
    a = [2555]

    nonlocal c
    c = [32564, 'hhhdd']

    return value % 2, - value


a = d.sort(key=my_sort(d))
print(a)
