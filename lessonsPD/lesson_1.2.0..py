def get_value_type():
    test_list = [369, 'Жил-был бродобрей', None, True]
    print('Типы значений в списке')
    for index, el in enumerate(test_list):  # Для красоты
        type_el = type(el)
        print(f'{index}. Значение: {el}; Тип: {type_el}')


def exchange_values():
    user_values = list(input('Введите значения для формирования списка. \n'))
    print('Введены значения: ', user_values)
    divisible_list = len(user_values) % 2 == 0
    get_range = (len(user_values) - 1, len(user_values))[divisible_list]  # Очень интересная штука - тернарные операторы
    i = 0
    while i < get_range:
        el = user_values
        el[i], el[i + 1] = el[i + 1], el[i]
        i += 2
    print('Получен список: ', user_values)


get_value_type()
exchange_values()
