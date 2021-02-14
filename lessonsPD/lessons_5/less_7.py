"""
7.	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь
(со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json


def get_dicts():
    """
    Создание словаря с исходными данными и значением доходности
    :return: [{'firm_1': 25000, 'firm_2': -500,..}, {“average_profit”: 2000}]
    """
    with open('for_less_7.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    firms = {}
    count_for_av = 0
    for line in lines:
        try:
            name, form, profit, costs = line.strip('\n').split(' ')
            firms.update({name: int(profit) - int(costs)})
            count_for_av += (0, 1)[int(profit) - int(costs) > 0]
        except ValueError:
            continue
    average_profit = {'average_profit': int(sum(val for val in firms.values() if val > 0) / count_for_av)}
    result = [firms, average_profit]
    return result


def write_firm_list_json():
    with open('for_less_7.json', 'w', encoding='utf-8') as file:
        json.dump(get_dicts(), file)


write_firm_list_json()
