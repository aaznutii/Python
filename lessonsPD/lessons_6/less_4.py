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
    is_police = False
    count = 0

    def __init__(self, speed, color, name, turn, is_police=False):
        self.count += 1
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
        self.get_status(turn)
        print('----------------------')

    def get_status(self, turn=None):  # Возможно усложняю, сделал для упорядочевания инит
        if self.speed == 0:
            self.stop()
        else:
            if turn is None:
                self.go()
            else:
                self.turn(turn)

    def go(self):
        print('Автомобиль поехал прямо')
        self.show_speed()

    def stop(self):
        if self.speed == 0:
            print('Автомобиль остановился')

    def turn(self, turn):
        turns = ['налево', 'на лево', 'лево', 0, 'left']
        code = ('Автомобиль повернул налево', 'Автомобиль повернул направо')[turn not in turns]
        print(code)
        self.show_speed()

    def show_speed(self):
        speed = self.speed
        print(f'Скорость автомобиля {speed}')
        if self.is_police is True:
            print('Полицейская машина')


class TownCar(Car):
    def __init__(self, speed, color, name, turn=None):
        print(f'TownCar: {name}, {color}')
        super().__init__(speed, color, name, turn, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
            print(f'Скорость автомобиля {self.speed}')
        else:
            print(f'Скорость автомобиля {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, turn=None):
        print(f'SportCar: {name}, {color}')
        super().__init__(speed, color, name, turn, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name, turn=None):
        print(f'WorkCar: {name}, {color}')
        super().__init__(speed, color, name, turn, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
            print(f'Скорость автомобиля {self.speed}')
        else:
            print(f'Скорость автомобиля {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, turn=None):
        print(f'PoliceCar: {name}, {color}')
        super().__init__(speed, color, name, turn, is_police=True)


test = TownCar(1, 'red', 'Lexus')
test1 = SportCar(70, 'dlu', 'Jaguar', 'Право')
test2 = WorkCar(60, 'green', 'Камаз', 'лево')
test3 = PoliceCar(10, 'Red', 'Lexus', 0)
test4 = TownCar(100, 'Red', 'Lexus', 1)
