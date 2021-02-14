"""
1.	Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""


def write_txt(value, file):
    with open(file, 'a', encoding='utf-8') as file:
        file.write(str(value) + '\n')


def add_to_file():
    print('Введите значения для создания файла или добавления в файл.\n')
    file_name = "for_less_1.txt"
    status_value = 0
    while status_value != 1:
        user_value = input()
        status_value = (write_txt(user_value, file_name), 1)[user_value == '']


add_to_file()
