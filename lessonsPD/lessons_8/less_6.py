"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""


class StatusValue(Exception):
    status = True

    def __init__(self, value):
        self.value = value
        self.get_status(value)

    def get_status(self, value):
        if value.isnumeric():
            self.status = True
        else:
            try:
                float(value)
                self.status = True
            except ValueError:
                self.status = False
