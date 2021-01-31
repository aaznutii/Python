# Без этой библиотеки никак не получается корректно распознать кортеж из файла

import ast


# Проверка введенного значения, перевод в соответствующий формат
def input_value(values):
    value = ''.join(values)  # Убрать пробелы
    if value.isnumeric():
        user_value = int(value)
    else:
        try:
            float(value)
            user_value = float(value)
        except ValueError:
            user_value = values
    return user_value


def count_for_products():  # Счет числа строк для получения индекса + 1
    count_name = 0
    with open('lists.txt', 'r') as file:
        for line in file:
            count_name += 1
    return count_name + 1


def append_lists(values, files):  # Записать в конец файла
    try:
        with open(files, 'a', encoding='utf-8') as file:  # Дозапись
            file.write(values + '\n')
    except FileExistsError:
        with open(files, 'w', encoding='utf-8') as file:  # Перезапись, или создание нового
            file.write(values + '\n')


def read_lists():  # Получение кортежей из файла для последующей работы
    lst = []
    with open('lists.txt', 'r', encoding='utf-8') as file:  # безопасное чтение файла
        for line in file:
            try:  # Попытка, если преобразование нормльно происходит
                ast_line = ast.literal_eval(line)
                lst.append(ast_line)
            except ValueError:  # На случай, если есть пустая строка
                continue
    return lst  # Возвращаем заполненный список кортежей


def create_analytics_dict():
    lst = read_lists()
    analytics = {'name': [], 'price': [], 'count': [], 'units': []}
    dict_to_list = []
    for tup in lst:  # кортежи. начинаем перебор строк по вертикали
        for key, val in tup[1].items():  # Берем горизонталь по индексу. пара ключ: значение - кортежи!
            # Условие по ключам для добавления. Никак не получается прикрутить сюда условие на значения
            if key in analytics.keys():
                analytics[key].append(val)  # заполняем по нужной форме словарь (пока со всеми значениями)

    for key, val in analytics.items():  # Цикл для перебора и прогонки через множества всех значений
        val = list(set(val))  # оставляем только уникальные значения
        dicts = {key: val}
        dict_to_list.append(dicts)  # получаем итоговую форму.
    append_lists(str(dict_to_list), 'for_analysis.txt')
