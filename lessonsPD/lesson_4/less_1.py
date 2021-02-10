"""
Задание 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
значений необходимо запускать скрипт с параметрами.

Иногда винда ругается и требует уточнить инструкцию для запуска скрипта. Для решения проблемы см. описание.
Для этого файла инструкция следующая: python ".\script_get_wages.py" first_param, second_param, third_param
"""
from sys import argv

script_name, first_param, second_param, third_param = argv
print(f'Расчет заработной платы скриптом: {script_name}\n')


def get_wages():
    """
    функция расчёта заработной платы сотрудника
    :return: summa
    """
    values = []
    for el in argv[1:]:  # argv возвращает список значений. Каждое значение str.
        try:
            el.isdigit()
            values.append(int(el))
        except ValueError:
            print('Вы ввели не число.')
            break
    summa = (values[0] * values[1]) + values[2]
    print(f'Итого заработная плата струдника составила: {summa} денег\n ')


get_wages()
