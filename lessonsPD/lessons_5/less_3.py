"""
3.	Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""


def get_workers():
    """
    Запись данных из файла в словарь
    :return: {'Скриптов': 100000,..}
    """
    with open("for_less_3.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
    workers = {}
    for line in lines:
        try:
            name, money = line.strip('\n').split(' ')
            workers.update({name: int(money)})
        except ValueError:
            continue
    return workers


def get_needy():
    workers = get_workers()
    needing = [name for name in workers if workers.get(name) < 20000]
    print(f'Получают заработную плату менее 20 000: {needing}')


def get_average():
    workers = get_workers()
    average = sum(workers.values()) / len(workers)
    print(f'Средняя величина дохода сотрудников :{average}')


get_needy()
get_average()
