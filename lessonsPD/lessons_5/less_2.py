"""
2.	Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов
в каждой строке.
"""


def get_count():  # Задача выполнена, но строка генератора получилась слишком сложная
    with open("for_less_1.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words = [len(word.split(' ')) for word in [el.strip('\n') for el in lines if el.strip('\n') != '']]
    print(f'Всего строк в файле: {len(lines)}')
    print(f'Всего слов в файле: {sum(words)}')


get_count()
