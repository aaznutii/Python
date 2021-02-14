"""
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Dress(ABC):
    size = 0

    @abstractmethod
    def amount_of_fabric(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Dress):
    count = 0

    def __init__(self, size):
        self.size = size

    @property
    def amount_of_fabric(self):
        result = self.size / 6.5 + 0.5
        self.count += 1
        return result

    def __add__(self, other):
        result = self.amount_of_fabric + other.amount_of_fabric
        return f'Всего для создания {self.count} пальто необходимо ткани: {result:.2f}\n' \
               f'___________'

    def __str__(self):
        return f'Для создания пальто необходимо :{self.amount_of_fabric:.2f} метров ткани'


class Suit(Dress):
    count = 0

    def __init__(self, size):
        self.size = size

    @property
    def amount_of_fabric(self):
        result = 2 * self.size + 0.3
        self.count += 1
        return result

    def __add__(self, other):
        result = self.amount_of_fabric + other.amount_of_fabric
        return f'Всего для создания {self.count} костюмов необходимо ткани: {result:.2f}\n' \
               f'___________'

    def __str__(self):
        return f'Для создания костюма необходимо :{self.amount_of_fabric:.2f} метров ткани'


c = Coat(50)
print(c)
c1 = Coat(60)
print(c1)
print(c + c1)

s = Suit(30)
s2 = Suit(40)
print(s)
print(s2)
print(s + s2)
