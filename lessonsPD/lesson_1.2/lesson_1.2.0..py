"""
В этом файле первые 5 задач.
Для проверки работы
"""
user_values = {'value': '', 'status': 0, 'rating': [6, 5, 4, 3, 2, 1], 'control_rating': []}


# Служебные функции


def input_value(text):  # Проверка введенного значения. Целое, с точкой, текст.
    user_values['value'] = input(text)  # Вводим значение и записываем в словарь
    if user_values['value'].isnumeric():  # Если введено целое число: 0
        user_values['status'] = 0  # Определяем статус введенного значения
    else:  # Если целое с точкой: 1
        try:
            float(user_values['value'])
            user_values['status'] = 1
        except ValueError:  # Если остальное (текст или текст и цифры): 2
            user_values['status'] = 2


def agree_user():  # Проверка согласия пользоваеля на действия
    answer = input('Введите "да" если согласны или любой другой символ для отмены. \n').lower()
    ag_list = ['да', 'y', 'yes']
    yes_var = (0, 1)[answer in ag_list]  # Очень интересная штука - тернарные операторы
    return yes_var


# функции задания


def get_value_type():  # Сравнение значений и их типов
    test_list = [369, 'Жил-был бродобрей', None, True]
    print('\nТипы значений в списке. Задание 1:')
    for index, el in enumerate(test_list):  # Для красоты
        type_el = type(el)
        print(f'{index}. Значение: {el}; Тип: {type_el}')


def exchange_values():  # Перестановка значений
    input_value('\nВведите значения для формирования списка и перестановки значений.\n')
    value = list(user_values['value'])
    print('Введены значения: ', value)
    divisible_list = len(value) % 2 == 0  # Если длинна кратна 2м - то оставляем длинну или вычитаем 1
    get_range = (len(value) - 1, len(value))[divisible_list]  # Очень интересная штука - тернарные операторы
    i = 0
    while i < get_range:
        value[i], value[i + 1] = value[i + 1], value[i]
        i += 2
    print('Получен список: ', value)


def change_season():  # Определение сезона
    seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
    message = '\nДля определения времени года укажите месяц. Введите целое число. \n'
    input_value(message)
    while user_values['status'] != 0 or int(user_values['value']) > 12:  # Проверка ошибки ввода
        input_value(message)
    value = int(user_values['value'])
    for key, val in seasons.items():  # В паре ключ:значение при обнаружении совпадения выбираем ключ
        if value in val:
            print(key)


def change_words():  # Вывод слов по шаблону
    input_value('\nВведите несколько слов через пробелы для получения нумерованного перечня.\n')
    to_list = user_values['value'].split(' ')
    for index, el in enumerate(to_list):
        print(f'{index + 1}. {el[:10]}')


def set_rating():  # Немного усложнил задачу. Пользователь может сначала сформировать рейтинг
    rating_str = user_values['rating']  # Обращаемся по ключу к словарю для записи значений.
    iteration = 0  # Переменная, для счета итераций цикла, чтобы разделить условия показа message
    user_values['status'] = 0  # Очищаем значение статуса введенного значения перед созданием рейтинга
    control = user_values['control_rating']  # Вводим контрольное значение.

    text = ['Введите цифру для включения в рейтинг. \n'
            'Для того, чтобы перестать вводить значения, введите любую букву, или нажмите Enter \n',
            'Значение добавлено в рейтинг. Продолжайте ввод.\n']

    while user_values['status'] == 0:  # Цикл позволяет вводит любое количество значений, пока вводится цифра.
        message = (text[1], text[0])[iteration == 0]
        input_value(message)
        if user_values['status'] == 0:
            control.append(user_values['value'])  # контроль введенных значений
            rating_str.append(int(user_values['value']))
            iteration += 1
    rating_str.sort(reverse=True)  # Сортировка данных по уменьшению
    print('Результирующий рейтинг:', rating_str)


def update_rating():  # Изменение рейтинга или его перезапись
    print('\n Функция изменения рейтинга или его перезаписи.\n'
          'Желаете сформировать рейтинг заново?\n'
          'Длинна рейтинга сейчас составляет:', len(user_values['rating']))
    if agree_user() == 1:
        user_values['rating'] = []
        set_rating()
    else:
        print('Внесите данные в существующий рейтинг.\n')
        set_rating()
    print('Вы ввели следующие значения:', user_values['control_rating'], '\n'
                                                                         'Длинна рейтинга сейчас составляет:',
          len(user_values['rating']))


def main():
    """
    Если нужно погонять конкретную функцию, можно закомменировать остальные.
    Сейчас закомментированны рабочие функции, которые не выдают непосредственные результаты задания.
    """
    # input_value("Тестовый текст")
    # agree_user()
    # set_rating()

    get_value_type()
    exchange_values()
    change_season()
    change_words()
    update_rating()


if __name__ == '__main__':
    main()
