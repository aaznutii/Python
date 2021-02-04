"""
4.	Реализуйте базовый класс Car.
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = bool

    def go(self):
        if self.speed > 0:
            print('Автомобиль поехал')
            self.show_speed()

    def stop(self):
        if self.speed == 0:
            print('Автомобиль остановился')

    def turn(self):
        print('Автомобиль певернул налево')
        print('Автомобиль певернул направо')
        print('Автомобиль развернулся')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')


class TownCar(Car):
    super().is_police = False

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
