"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Warehouse:
    pass


class OfficeEquipment(Warehouse):
    name = ''
    color = ''
    count = 0
    weight = 0
    size = [0, 0, 0]
    cost = 0


class Printer(OfficeEquipment):
    def __init__(self, name, color, count, weight, size, cost, print_speed):
        self.name = name
        self.color = color
        self.count = count
        self.weight = weight
        self.size = size
        self.cost = cost
        self.print_speed = print_speed


class Scaner(OfficeEquipment):
    pass


class Copier(OfficeEquipment):
    pass


p = Printer()
