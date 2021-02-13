"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
# Возможно не до конц понял задание. Пока сделал так.

class Date:

    def __init__(self, date):
        """"
        input date:  dd-mm-yyyy
        """
        self.date = date
        self.validation_int(self.get_int(date))

    @classmethod
    def get_int(cls, date):
        try:
            date_list = [int(el) for el in date.split('-')]
            return date_list
        except ValueError:
            print('Ошибка. Введен текст.\n'
                  'Введите корректно дату в формате dd-mm-yyyy')
            return False

    @staticmethod
    def validation_int(list):
        if list is False:
            return
        else:
            default = (['day', 31], ['month', 12], ['years', 3000])
            result = []
            for i, el in enumerate(list):
                if el == 0 or el > default[i][1]:
                    print(f'Некорректно укзана дата. Исправьте {default[i][0]}')
                    break
                else:
                    result.append(str(el))
            if len(result) == 3:
                result = ':'.join(result)
                print(f'Введена дата: {result}')


d = Date('12-12-2021')
