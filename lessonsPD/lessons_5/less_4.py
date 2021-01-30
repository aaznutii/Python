"""
4.	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


def get_file(file_name, mode, values=None):  # Хорошая функция для открытия файла. универсальненько
    """
    Открывет файл для записи/создания или чтения в зависимости от наличия значений для записи
    :param file_name:
    :param mode:
    :param values:
    """
    with open(file_name, mode, encoding='utf-8') as file:
        if values is None:
            lines = file.readlines()
            return lines
        else:
            file.write(values)


def get_numbers():
    """
    Создание словаря с исходными значениями
    :return: {1: 'One ', 2: 'Two ', 3: 'Three ', 4: 'Four '}
    """
    lines = get_file('for_less_4.txt', 'r')
    numbers = {}
    for line in lines:
        try:
            name, number = line.strip('\n').strip(' ').split('—')
            numbers.update({int(number): name})
        except ValueError:
            continue
    return numbers


def rewrite_numbers():
    numbers = get_numbers().copy()  # По условиям задания должны быть произведена замена значения. Потому copy
    print(f'Данные исходного списка: {numbers}')
    file_name = input('Укажите название файла для сохранения данных\n')
    rus_names = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    for key, name in numbers.items():
        if key in rus_names.keys():
            numbers[key] = rus_names[key]
    for key, name in numbers.items():
        get_file(file_name, 'a', f'{name} - {key}\n')
    print(f'Получены данные: {numbers}')
    print(f'Данные сохранены по форме в файл {file_name}')


rewrite_numbers()
