"""
3.	Реализовать базовый класс Worker (работник).

●	определить атрибуты: name, surname, position (должность), income (доход);
●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
 например, {"wage": wage, "bonus": bonus};
●	создать класс Position (должность) на базе класса Worker;
●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
 премии (get_total_income);
●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.

"""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self):
        money = super()._income
        result = money['wage'] + money['bonus']
        print(f'{result}')

    def __init__(self, name, surname, position, income_wage, income_bonus):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income = {"wage": income_wage, "bonus": income_bonus}
        self.get_full_name()
        self.get_total_income()


test_p = Position('Василий', 'Пупкин', 'meneg', 20000, 5000)
