"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZeroExc(Exception):
    """Деление на ноль"""
    pass


def get_status_division(number1, number2):
    try:
        if number2 == 0:
            raise ZeroExc('Ошибка.Деление на ноль')
        result = number1 / number2
        print(result)
    except ZeroExc as z:
        print(z)


number_list = [2, 0, 5, 9, -10, 0]

for el in number_list:
    get_status_division(10, el)
