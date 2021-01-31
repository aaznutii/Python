"""
5.	Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""


def open_file(file_name='for_less_5.txt', mode='r', values=None):
    """
    Открывет файл для записи/создания или чтения в зависимости от наличия значений для записи
    :param file_name: 'for_less_5.txt'
    :param mode: 'r'
    :param values: 'values'
    """
    with open(file_name, mode, encoding='utf-8') as file:
        if values is None:
            lines = file.readlines()
            return lines
        else:
            file.write(values)


def write_input_number():
    """
    Ввод цифр через пробел, их запись в файл до момента пустого ввода "Enter". Файл перезаписывается.
    Проводится проверка, что введены цифры.
    """
    print('Введите цифры. Цифры будут записаны в файл.'
          'Для прекращения ввода нажмите Ввод')
    var_dict = {'user_numbers': [], 'stop': 0}
    while var_dict['stop'] == 0:
        user_values = input().split(' ')
        for el in user_values:
            if el.isnumeric():
                var_dict['user_numbers'].append(el + ' ')
            else:
                var_dict['stop'] = 1
                break
    open_file("for_less_5.txt", 'w', ''.join(var_dict['user_numbers']))
    print('Введенны числа и записаны в файл: {}'.format(''.join(var_dict['user_numbers'])))


def sum_numbers_from_file():
    """
    Суммирование цифр из файла, вызов функци добавления цифр и записи в файл.
    """
    write_input_number()
    numbers = ' '.join(open_file('for_less_5.txt', 'r')).split()
    sum_numbers = sum([int(el) for el in numbers])
    print(f'Итого сумма цифр в файле: {sum_numbers}')


sum_numbers_from_file()
