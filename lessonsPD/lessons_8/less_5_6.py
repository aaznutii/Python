"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""
import pickle

import less_6


class Warehouse:
    places = ('warehouse', 'home', 'office')
    categories = ['Printer', 'Scanner', 'Copier']

    @staticmethod
    def add_products():
        for i, el in enumerate(Warehouse.categories):
            print(f'Код: {i}. Категория: {el}')
        user_inp = input('Введите числовой код категории:\n ________\n')
        result = Warehouse.categories[int(user_inp)]
        print(f'Вы выбрали категорию {result}')
        working_class = eval(result)
        attributes = working_class.attributes.split(', ')

        def input_values_list(attributes):
            values_list = []
            print('Введите поочередно значения\n')
            for value in attributes:
                user_value = input(f'Введите {value}: ')
                values_list.append(user_value)
            return values_list

        result_list = input_values_list(attributes)

        def get_valid_val(result_list):
            print('Производится контроль введенных значений')
            result_str = ''
            for k, val in enumerate(result_list):
                if less_6.StatusValue(val).status is False and k < 2:
                    result_str += f'"{val}", '
                elif less_6.StatusValue(val).status is True and k >= 2:
                    result_str += (f'{val}, ', f'{val}')[len(result_list) - 1 == k]
                else:
                    print(f'Вы допустили ошибку при введении данных: {val}. '
                          f'Данные не сохранены. Желаете продожить?')
                    result_str = None
                    if agree_user() == 1:
                        Warehouse.add_products()
                    else:
                        return None
            print("Значения приняты")
            return result_str

        values = get_valid_val(result_list)

        def get_place():
            if values is None:
                return
            else:
                for k, pl in enumerate(Warehouse.places):
                    print(f'Код: {k}. Место хранения: {pl}')
                user_choice = input('Выберите где будет размещаться продукт: ')

            new_instance = eval(f'{result}({values})')
            res = (Warehouse.places[int(user_choice)], new_instance.get_dict())
            get_file(res)

        get_place()


class OfficeEquipment:
    name = ''
    color = ''
    count = 0
    weight = 0
    size = [0, 0, 0]
    cost = 0

    def get_dict(self):
        result = {'name': self.name, 'color': self.color,
                  'count': self.count, 'weight': self.weight,
                  'size': self.size, 'cost': self.cost}
        return result

    def get_place(self):
        pass


class Printer(OfficeEquipment):
    attributes = 'name, color, count, weight, we, le, he, cost, print_speed'

    def __init__(self, name, color, count, weight, we, le, he, cost, print_speed):
        self.name = name
        self.color = color
        self.count = count
        self.weight = weight
        self.size = [we, le, he]
        self.cost = cost
        self.print_speed = print_speed

    def get_dict(self):
        result = OfficeEquipment.get_dict(self)
        result['print_speed'] = self.print_speed
        return result


class Scanner(OfficeEquipment):
    attributes = 'name, color, count, weight, we, le, he, cost, scan_speed'

    def __init__(self, name, color, count, weight, we, le, he, cost, scan_speed):
        self.name = name
        self.color = color
        self.count = count
        self.weight = weight
        self.size = [we, le, he]
        self.cost = cost
        self.scan_speed = scan_speed

    def get_dict(self):
        result = OfficeEquipment.get_dict(self)
        result['scan_speed'] = self.scan_speed
        return result


class Copier(OfficeEquipment):
    attributes = 'name, color, count, weight, we, le, he, cost, count_copy'

    def __init__(self, name, color, count, weight, we, le, he, cost, count_copy):
        self.name = name
        self.color = color
        self.count = count
        self.weight = weight
        self.size = [we, le, he]
        self.cost = cost
        self.count_copy = count_copy

    def get_dict(self):
        result = OfficeEquipment.get_dict(self)
        result['count_copy'] = self.count_copy
        return result


# Файл формата .pkl позволяет сохранять структуры python в исходном виде
def get_file(new_strukture=None):
    if new_strukture is not None:
        with open('products.pkl', 'ab') as file:
            pickle.dump(new_strukture, file)
            print('Данные записаны')
    else:
        with open('products.pkl', 'rb') as file:  # ВАЖНО: загрузка считывает один объект за раз. Следоательно: цикл
            result = []
            while True:
                try:
                    f = pickle.load(file)
                    result.append(f)
                except EOFError:
                    break
            return result


def agree_user():
    """
    Проверка согласия пользоваеля на действия
    :return: 0 | 1 - если согласен
    """
    answer = input('Введите "да" или 1, любой другой символ для отмены. \n').lower()
    ag_list = ['да', 'y', 'yes', '1']
    yes_var = (0, 1)[answer in ag_list]
    return yes_var


def main():
    print('Приветствуем вас в программе "Склад"\n'
          'Желаете ввести новые данные?')
    if agree_user() == 1:
        print('Желаете загрузить данные из списка?')
        if agree_user() == 1:
            print('Напоминаем, структура данных должна соответствовать форме:\n'
                  'name, color, count, weight, we, le, he, cost, count_copy')
        else:
            print("Выбран ручной ввод данных.")
            Warehouse.add_products()
    else:
        print('Желаете посмотреть данные?')
        if agree_user() == 1:
            f = get_file()
            for el in f:
                print(el)
        else:
            print('Выход из программы')


if __name__ == '__main__':
    main()