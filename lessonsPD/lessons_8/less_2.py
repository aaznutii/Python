"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZeroExc(Exception):
    def __init__(self, number1, number2):
        self.get_status_division(number1, number2)

    def get_status_division(self, number1, number2):
        try:
            result = number1 / number2
            print(result)
        except ZeroDivisionError:
            print('Деление на ноль')


z = ZeroExc(5, 0)
z1 = ZeroExc(5, 1)
z2 = ZeroExc(-2, 0)
z3 = ZeroExc(5, 15)
