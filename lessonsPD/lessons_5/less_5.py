"""
5.	Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""


def open_file(file_name, mode, values=None):
    """
    Открывет файл для записи/создания или чтения в зависимости от наличия значений для записи
    :param file_name: 'for_less_4.txt'
    :param mode: 'r'
    :param values: 'values'
    """
    with open(file_name, mode, encoding='utf-8') as file:
        if values is None:
            lines = file.readlines()
            return lines
        else:
            file.write(values)


def input_number():
    """
    Ввод цифр через пробел, их запись в файл до момента ввода "!"
    """
    print('Введите цифры, разделенные пробелами. Цифры будут записаны в файл.'
          'Для прекращения ввода введите любую букву')
    var_dict = {'user_numbers': [], 'stop': 0}
    while var_dict['stop'] == 0:
        user_values = input().split(' ')
        for el in user_values:
            if el.isnumeric():
                var_dict['user_numbers'].append(int(el))
            else:
                var_dict['stop'] = 1
                break
        print('Введенны числа и записаны в файл: {}'.format(sum(var_dict['user_numbers'])))


# Запуск Задание 5
input_number()
