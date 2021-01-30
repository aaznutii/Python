"""
2.	Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов
в каждой строке.
Не страшно,ведь,  что я ипользую уже имеющийся файл txt
"""


def get_count_new():
    """
    Слили строки воедино, разделили по пробелам и отбросив лишниее знаки посчитали слова.

    """
    with open("for_less_1.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
    words = [el.strip('\n').strip('.') for el in ' '.join(lines).split(' ') if el.strip('\n') != '']
    print(f'Всего строк в файле: {len(lines)}')
    print(f'Всего слов в файле: {len(words)}')


get_count_new()
