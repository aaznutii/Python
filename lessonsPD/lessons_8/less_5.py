"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""
import datetime
from abc import ABC, abstractmethod


class Warehouse:
    count = 0


class OfficeEquipment:
    name = ''
    color = ''
    count = 0
    weight = 0
    size = [0, 0, 0]
    cost = 0

    # volume = 5000  # Вместительность склада метров куб.

    # Сложение для получения складской сводки
    # def __add__(self, other):
    #     self.count = self.count + other.count
    #     self.weight = self.weight + other.weight
    #     self.size = [el + i for el, i in zip(self.size, other.size)]
    #     self.cost = self.cost + other.cost
    # self.volume = self.volume - (lambda x, y: x * y(self.size))
    # return

    # @abstractmethod
    def get_dict(self):
        result = {'name': self.name, 'color': self.color,
                  'count': self.count, 'weight': self.weight,
                  'size': self.size, 'cost': self.cost}
        return result


class Printer(OfficeEquipment):
    def __init__(self, name, color, count, weight, we, le, he, cost, print_speed):
        # self.name = name
        # self.color = color
        # self.count = count
        # self.weight = weight
        # self.size = [we, le, he]
        # self.cost = cost
        self.print_speed = print_speed

    def get_dict(self):
        OfficeEquipment.get_dict()
        result = {'name': self.name, 'color': self.color,
                  'count': self.count, 'weight': self.weight,
                  'size': self.size, 'cost': self.cost, 'print_speed': self.print_speed}
        return result


class Scanner(OfficeEquipment):
    def __init__(self, name, color, count, weight, we, le, he, cost, scan_speed):
        self.name = name
        self.color = color
        self.count = count
        self.weight = weight
        self.size = [we, le, he]
        self.cost = cost
        self.scan_speed = scan_speed

    def get_dict(self):
        result = {'name': self.name, 'color': self.color,
                  'count': self.count, 'weight': self.weight,
                  'size': self.size, 'cost': self.cost, 'print_speed': self.scan_speed}
        return result


class Copier(OfficeEquipment):
    def __init__(self, name, color, count, weight, we, le, he, cost, count_copy):
        self.name = name
        self.color = color
        self.count = count
        self.weight = weight
        self.size = [we, le, he]
        self.cost = cost
        self.count_copy = count_copy

    def get_dict(self):
        result = {'name': self.name, 'color': self.color,
                  'count': self.count, 'weight': self.weight,
                  'size': self.size, 'cost': self.cost, 'print_speed': self.count_copy}
        return result


p = Printer('hp', 'red', 1, 5, 15, 10, 20, 25000, 30)
p2 = Printer('Canon', 'white', 1, 5, 15, 10, 20, 20000, 30)
print(p.name)
print(p.size)
print(p.get_dict())

# def main():
#
#
#     if __name__ == '__main__':
#         main()
#
