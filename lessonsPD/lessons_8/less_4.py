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
    def __init__(self, name, color, count, weight, we, le, he, cost, print_speed):
        self.name = name
        self.color = color
        self.count = count
        self.weight = weight
        self.size = [we, le, he]
        self.cost = cost
        self.print_speed = print_speed


class Scaner(OfficeEquipment):
    def __init__(self, name, color, count, weight, we, le, he, cost, scan_speed):
        self.name = name
        self.color = color
        self.count = count
        self.weight = weight
        self.size = [we, le, he]
        self.cost = cost
        self.print_speed = scan_speed


class Copier(OfficeEquipment):
    def __init__(self, name, color, count, weight, we, le, he, cost, count_copy):
        self.name = name
        self.color = color
        self.count = count
        self.weight = weight
        self.size = [we, le, he]
        self.cost = cost
        self.print_speed = count_copy


p = Printer('hp', 'red', 1, 5, 15, 10, 20, 25000, 30)
print(p.name)
print(p.size)
