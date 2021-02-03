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
from itertools import cycle


# Первый вариант. Здесь, судя по всему, класс подобен классической фнкции.
# class TrafficLight:
#     # Атрибут класса
#     _color = {'Красный': 7, 'Жёлтый': 2, 'Зеленый': 7}
#
#     # Метод класса
#     def running(self):
#         count = 0
#         while count < 6:
#             for name, sec in TrafficLight._color.items():
#                 print(f'Светит: {name}; время: {sec}')
#                 time.sleep(sec)
#                 count += 1
#                 print(count)


# Третий вариант.
# class TrafficLight:
#     # Атрибут класса
#     _color = ('Красный', 'Жёлтый', 'Зеленый')
#
#     # Метод класса
#     def running(self):
#         for i in range(len(TrafficLight._color)):
#             print(TrafficLight._color[i])
#             time.sleep(int(self.seconds[i]))
#
#     def __init__(self):
#         print('Введите через пробел время для каждого режима (Красный, жёлтый, зеленый) '
#               'или оставьте время по умолчанию и введите Enter')
#         user_values = input().split()
#         self.seconds = (user_values, [7, 2, 5])[user_values == []]
#         self.running()

# test = TrafficLight()
# test.running()


class TrafficLight:
    # Атрибут класса
    _color = ''

    # Метод класса
    def running(self, color):
        colors = ('Красный', 'Жёлтый', 'Зеленый')
        seconds = [7, 2, 5]
        print(color)
        time.sleep(seconds)


#
#
test = TrafficLight()
test.running()
test2 = TrafficLight()
test2.running()
test3 = TrafficLight()
test3.running()
test4 = TrafficLight()
test4.running()
