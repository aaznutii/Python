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
from abc import ABC


class Dress(ABC):
    size = 0


class Coat(Dress):
    def amount_of_fabric(self, size):
        result = int(size) / 6.5 + 0.5
        return result


class Suit(Dress):
    def amount_of_fabric(self, size):
        result = 2 * int(size) + 0.3
        return result


c = Coat().amount_of_fabric(50)
print(c)
c1 = Coat().amount_of_fabric(70)
print(c1)
print(c + c1)

s = Suit().amount_of_fabric(50)
s2 = Suit().amount_of_fabric(30)
print(s)
print(s2)
print(s + s2)
print(c + c1 + s + s2)

"""
# класс Auto
class Auto:

    # конструктор класса Auto
    def __init__(self, year):
        # Инициализация свойств.
        self.year = year

    # создаем свойство года
    @property
    def year(self):
        return self.__year

    # сеттер для создания свойств
    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году"

a = Auto(2090)
print(a.get_auto_year())

"""
