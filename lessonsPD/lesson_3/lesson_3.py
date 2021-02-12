# Задание 1
def division_num(num_1, num_2):  # По условиям задания должны приниматься значения.
    """
    Деление
    :param num_1: 4
    :param num_2: 2
    :return: 2
    """
    values = {'num_1': num_1, 'num_2': num_2, 'control': 0}
    while values['control'] == 0:  # Ввел цикл с проверкой ввода
        try:
            result = int(values['num_1']) / int(values['num_2'])
            print(f'Вы ввели следующие числа: {num_1}, {num_2}. В результате деления получилось:{result}')
            values['control'] = 1
        except ZeroDivisionError:
            values['num_2'] = input('Вы ввели 0. Деление на ноль. Введите значение делителя заново\n')
            continue
        except ValueError:
            values['num_1'] = input('Вы ошиблись со вводом. Введите делимое\n')
            values['num_2'] = input('Введите делитель\n')


# Запуск Задание 1
# division_num(input('Введите делимое\n'), input("Введите делитель\n"))


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


# Запуск Задание 2
# user_data("Вася", "Обломов", "25 января 1904", "Москва", "jblomov@rai.ru", "8927000000")


# Задание 3
def sum_max_numbers(num_1, num_2, num_3):
    """
    Сумма двух максимальных чисел из трех
    :param num_1: 1
    :param num_2: 2
    :param num_3: 3
    :return: 5
    """
    num_list = [num_1, num_2, num_3]
    sum_max = sum(num_list) - min(num_list)  # Чисел всего три. Достаточно суммировать и вычесть минимальное.
    return sum_max


# Запуск Задание 3
# print(sum_max_numbers(9, 2, 1))


# Задание 4
def my_func(x, y):
    # values = {'x': x, 'y': y}
    """
    Возведене в отрицательную степень по формуле 1/(x**y). Два способа.
    :param x: 4
    :param y: -2
    :return:0.0625
    """
    task_solution_1 = x ** y
    print('Первое решение: ', task_solution_1)

    def exponentiation(val_x, val_y):
        """
        Возведение в степень в цикле
        :param val_x:
        :param val_y:
        :return:
        """
        result = val_x
        for i in range(abs(val_y) - 1):
            result = result * val_x
        return result

    if y < 0:
        task_solution_2 = 1 / exponentiation(x, y)
        print('Второе решение: ', task_solution_2)
    else:
        task_solution_2 = exponentiation(x, y)
        print(f'Вы возводите не в отрицательную степень. Результат: {task_solution_2}')


# Запуск Задание 4
# my_func(4, -2)


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


# Запуск Задание 5
# sum_input_number()


# Задание 6
def int_funk(string):
    """
    Строка с большой буквы
    :param string:
    :return: String
    """
    result = string.capitalize()
    return result


# Запуск Задание 6
# print(int_funk("string"))


# Задание 7
def upper_first_lit():
    """
    Ввести строку, каждое слово с большой буквы.
    :return: String, String, String,..
    """
    values = input('Введите строку\n').split(' ')
    for el in range(len(values) - 1):
        values[el] = int_funk(values[el])
    print(' '.join(values))

# Запуск Задание 7
# upper_first_lit()
