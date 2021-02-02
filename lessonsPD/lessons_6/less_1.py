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
class TrafficLight:
    # Атрибут класса
    _color = ['Красный', 'Жёлтый', 'Зеленый']

    def running(self):
        for i in range(len(TrafficLight._color)):
            print(TrafficLight._color[i])
            time.sleep(int(self.seconds[i]))

    def __init__(self, color_index=0, seconds=7):
        self.color_index = color_index
        print('Введите через пробел время для каждого режима (Красный, жёлтый, зеленый) '
              'или оставьте время по умолчанию: 5 ')
        user_values = input().split()
        print(user_values)
        print(type(user_values))
        self.seconds = (user_values, [7, 2, 5])['' in user_values]
        self.running()


test = TrafficLight(0, 3)
