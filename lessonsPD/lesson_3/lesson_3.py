# Задание 1
def division_num(num_1, num_2):
    """
    Деление
    :param num_1: 4
    :param num_2: 2
    :return: 2
    """
    if num_2 != 0:
        result = num_1 / num_2
        print(f'Вы ввели следующие числа: {num_1}, {num_2}. В результате деления получилось:{result}')
    else:
        print('Вы ввели 0. Деление на ноль')


division_num(256, 8)


# Задание 2
def user_data(name, family, birthday, city, e_mail, telefone):
    """
    Печать данных пользователя одной строкой.
    :param name:
    :param family:
    :param birthday:
    :param city:
    :param e_mail:
    :param telefone:
    :return: Пользователь:{family,name} родился {birthday}в городе {city};
             Элктронная почта: {e_mail}.Телефон контакта: {telefone}
    """
    print(f'Пользователь:{" ".join([family, name])} родился {birthday}'
          f' в городе {city}; Элктронная почта: {e_mail}. '
          f'Телефон контакта: {telefone}')


user_data("Вася", "Обломов", "25 января 1904", "Москва", "jblomov@rai.ru", "8927000000")


# Задание 3
def sum_max_numbers(num_1, num_2, num_3):
    """
    Сумма двух максимальных чисел
    :param num_1: 1
    :param num_2: 2
    :param num_3: 3
    :return: 5
    """
    num_list = [num_1, num_2, num_3]
    sum_max = sum(num_list) - min(num_list)
    return sum_max


print(sum_max_numbers(1, 2, 3))


# Задание 4
def my_func(x, y):
    """

    :param x: 4
    :param y: -2
    :return:0.0625
    """
    task_solution_1 = x ** y
    print('Первое решение: ', task_solution_1)
    task_solution_2 = x
    for i in range(abs(y) - 1):
        task_solution_2 = task_solution_2 * x
    task_solution_2 = 1 / task_solution_2
    print('Второе решение: ', task_solution_2)


my_func(4, -2)


# Задание 5
def sum_input_number():
    """
    Ввод цифр через пробел, их суммирование до момента ввода "!"
    :return: Сумма введенных чисел до момента введения "!"
    """
    print('Введите цифры, разделенные пробелами. Цифры будут суммированы.'
          'Для выхода из программы нажмите "!"')
    var_dict = {'user_sum': 0, 'stop': 0}  # Использование словаря позволяет избежать проблем видимости
    while var_dict['stop'] == 0:
        user_value = input().split(' ')
        for el in user_value:
            if el.isnumeric():
                var_dict['user_sum'] = var_dict['user_sum'] + int(el)
            elif el == '!':
                var_dict['stop'] = 1
                break
        print('Сумма введенных чисел: {}'.format(var_dict['user_sum']))


sum_input_number()


# Задание 6
def int_funk(string):
    """
    Строка с большой буквы
    :param string:
    :return: String
    """
    result = string.capitalize()
    return result


print(int_funk("string"))


# Задание 7
def upper_first_lit():
    """
    Ввести строку, каждое слово с большой буквы.
    :return: String, String, String,..
    """
    values = input('Введите строку').split(' ')
    for el in range(len(values)):
        values[el] = int_funk(values[el])
    print(values)


upper_first_lit()
