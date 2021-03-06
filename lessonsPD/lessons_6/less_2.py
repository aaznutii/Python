"""
2.	Реализовать класс Road (дорога).
●	определить атрибуты: length (длина), width (ширина);
●	значения атрибутов должны передаваться при создании экземпляра класса;
●	атрибуты сделать защищёнными;
●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
●	проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _length = 0
    _width = 0

    def get_mass(self, _length, _width):
        result = (_length * _width * 25 * 5) / 1000
        return result


mass = Road().get_mass(20, 5000)
print(mass)
