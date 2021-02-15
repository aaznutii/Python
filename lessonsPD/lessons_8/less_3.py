"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


# Вариант 1 - если исходить из того функционала, который сформулировн для предполагаемого класса в задании.
# Вероятно я ошибаюсь, но такой функционал мало похож на задачи исключения
class StatusValue(Exception):
    status = True

    def __init__(self, value):
        self.value = value
        self.get_status(value)

    def get_status(self, value):
        if value.isnumeric():
            self.status = True
        else:
            try:
                float(value)
                self.status = True
            except ValueError:
                print(f"Введен текст: {value}. Данные не добавлены в список.")
                self.status = False


def get_numbers_list():
    numbers_list = []
    stop = 0
    print('Введите цифры, разделенные пробелами для добавления в список.\n'
          'Для выхода из программы нажмите "!" или введите пустое значение')
    while stop == 0:
        user_value = input().split(' ')
        for el in user_value:
            if el == '!' or el == '':
                stop = 1
                break
            elif StatusValue(el).status is True:
                numbers_list.append(el)
    print(f'Итоговый список: {numbers_list}')

# get_numbers_list()


# Вариант 2 - если исходить из назначения класса в задании. По образцу методички
# class OwnError(ValueError):
#     """Не число"""
#     def __init__(self):
#         self.err = ValueError(f"Данные не добавлены в список.")
#     # pass
#
#
# def get_numbers_list2():
#     numbers_list = []
#     stop = 0
#     print('Введите цифры, разделенные пробелами для добавления в список.\n'
#           'Для выхода из программы нажмите "!" или введите пустое значение')
#     while stop == 0:
#         value = input().split(' ')
#         for el in value:
#             if el == "!" or el == '':
#                 stop = 1
#                 break
#             else:
#                 if el.isnumeric():
#                     result = int(el)
#                     numbers_list.append(result)
#                 else:
#                     try:
#                         result = float(el)
#                         numbers_list.append(result)
#                     except ValueError:
#                         # print(f"Данные не добавлены в список.")
#                         raise OwnError()
#                     except OwnError():
#                         print(f"Введен текст: {el}.Данные не добавлены в список.")
#     print(numbers_list)
#
#
# get_numbers_list2()
