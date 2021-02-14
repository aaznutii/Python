"""
1.	Создать класс TrafficLight (светофор).
●	определить у него один атрибут color (цвет) и метод running (запуск);
●	атрибут реализовать как приватный;
●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего
(зелёный) — на ваше усмотрение;
●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
●	проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    # Атрибут класса
    __color = ''
    _count = 0

    # Метод класса
    def running(self, color, seconds):
        count = TrafficLight._count
        print(color)
        time.sleep(seconds)
        if count < 2:
            TrafficLight._count += 1
        else:
            TrafficLight._count = 0

    def __init__(self, __color, user_seconds=None):
        """
        :param _color: Ввести индекс цвета:Красный: 0, Желтый: 1, Зеленый: 2
        :param seconds: default = 7, 2, 5
        """
        def_colors = ('Красный', 'Жёлтый', 'Зеленый')
        def_seconds = [7, 2, 5]
        seconds = (user_seconds, def_seconds[self._count])[user_seconds is None]
        if __color == self._count:
            self.running(def_colors[__color], seconds)
        else:
            print('Нарушен порядок включения света')


test = TrafficLight(0, 3)
test2 = TrafficLight(1, 2)
test3 = TrafficLight(0, 2)
test4 = TrafficLight(2, 5)
test5 = TrafficLight(0, 7)
test6 = TrafficLight(2, 5)
test7 = TrafficLight(1, 2)
test8 = TrafficLight(2, 2)
test9 = TrafficLight(0)
