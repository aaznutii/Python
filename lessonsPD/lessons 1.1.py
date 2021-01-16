

"""
В этом файле я сформировал все домашние задания в виде функций таким образом, чтобы не привлекать сторонние библиотеки.
Все функции исполняются из main() в конце файла, чтобы можно было контролировать процес и очередность их запуска.
Логика: если запустить исполнение кода, то запуститься main(), из которой запустится остальное.
Функции удобны, поскольку исполнение кода не зависит от их физического положения в файле.

Для демонстрации работы с переменными во всем файле используется одна переменная user_value, которой присвоено значение 
словаря, разделяющего 2а типа переменных, исходя из контроля введенного пользователем значения: цифра и текст.
Значения словаря получаются и перезаписываются по индексу (имени 'var_number', например). Замечу, что даже в рамках 
одной функции значение переменной может быть перезаписано несколько раз.
Мне кажется, это удобнее чем глобальная переменная.

Вторая важная функция status_input_function(). Именно она отвечает за получение,проверку, запись типа введенного значени
На мой взгляд, функция status_input_function() имеет прикладной смысл. Я ее себе сохраню.
Хотя, наверняка есть другой путь.
"""

# Переменная со словарем для сохранения результата ввода. Словарь - это пара - имя(индекс): знчение
user_value = {'var_number': '0', 'var_text': ''}


def status_input_function(text):    # Проверка введенного значения. Целое, с точкой, текст, внесение в словарь.
    user_input = input(text)
    if user_input.isnumeric():                              # Если введено целое число
        status_input = 0                                    # Определяем стату как 0
        user_value['var_number'] = user_input               # Записываем по индексу в словарь
        print(f"Вы ввели целое число: {user_input}")
    else:
        try:
            # Функция float() пытается преобразовать значение в число с точкой.
            # Если введен текст, то будет сообщение об ошибке. Поэтому используется конструкция try except(см.гуглу)
            float(user_input)
            status_input = 1
            user_value['var_number'] = user_input
            print(f"Вы ввели число с точкой: {user_input}")
        except ValueError:                                  # Если введен текст
            status_input = 2
            user_value['var_text'] = user_input
            print(f"Вы ввели следующий текст: {user_input}")
    return status_input                                     # return Возвращает статус проверки: 0, 1, 2


def sec_to_time(text):                              # Перевод секунд во время и представление в нужном формате
    sec_count = {'for_min': 60, 'for_hour': 3600, 'for_day': 86400}
    # Собственно расчет времени арифметически, после подтверждения типа int
    if status_input_function(text) == 0:
        sec = int(user_value['var_number'])
        time_view = ['{}', '{}', '{}']          # Список для формирование маски ввода значений
        s = sec % sec_count['for_min']
        h = sec // sec_count['for_hour']
        m = (sec - (h * sec_count['for_hour'])) // sec_count['for_min']
        times = [h, m, s]
        for i in range(len(times)):       # Не знаю как добавить лишний ноль в строку с помощью .format, сделал в цикле
            if times[i] < 10:
                time_view[i] = '0{}'
        time_view = ':'.join(time_view)     # сформировал единую строку из списка
        print(time_view.format(h, m, s))
    else:
        sec_to_time('Введите секунды')


def n_function(text):                   # Сложение текста и цифр
    if status_input_function(text) == 0:
        n = user_value['var_number']
        n = int(n * 2) + int(n * 3) + int(n)
        print('Получется число: ', n)
    else:
        n_function(text)


def max_number(text):                   # Выбор наибольшего числа
    if status_input_function(text) == 0:
        n = user_value['var_number']
        n = list(n)                 # Превратили в список
        count = 0
        numbers = 0
        while count < len(n):
            if int(n[count]) > numbers:
                numbers = int(n[count])
                count += 1
            else:
                numbers = numbers
                count += 1
        print('Наибольшая цифра: ', numbers)
    else:
        max_number(text)


def my_firm(text):                          # Прибыль и убытки
    print(text)
    input_message = ['Введите значение выручки: ', 'Введите значение издержек: ', 'Сколько у Вас сотрудников?: ']
    if status_input_function(input_message[0]) == 0:
        revenue = int(user_value['var_number'])
        if status_input_function(input_message[1]) == 0:
            costs = int(user_value['var_number'])
            if revenue > costs:
                print('Вы в прибыли! Вы заработали: ', revenue-costs)
                status_input_function(input_message[2])
                people = int(user_value['var_number'])
                print('Рентабельность на одного человека персонала составляет: {:.2f}'.format((revenue-costs) / people))
            elif revenue == costs:
                print('Нулевая рентабельность. Может поменять сферу?', end='\n')
            else:
                print('Вы в убытках. Вы потеряли: ', revenue-costs)
        else:
            my_firm(text)
    else:
        my_firm(text)


def runner(text):               # Бегун
    print(text)
    input_message = ['Сколько бегун пробегает каждый день?: ', 'Сколько должен пробежать?: ']
    if status_input_function(input_message[0]) == 0:
        a = int(user_value['var_number'])
        if status_input_function(input_message[1]) == 0:
            b = int(user_value['var_number'])
            count_day = 0
            while a < b:
                a = (a / 10) + a
                count_day += 1
                print('{}-й день: {:.2f}'.format(count_day, a))
            print('Ответ: на {}-й день спортсмен достиг результата — не менее {:.2f} км'.format(count_day, b))
        else:
            runner(text)
    else:
        runner(text)


def main():
    input_message = ["Задание 1-е. Введите число для записи его в переменную user_value\n",
                     "Задание 2-е. Введите текст для записи его в переменную user_value\n",
                     "Задание 3. Введите количество секунд, которое необходимо преобразовать "
                     "в данные времени. Целое число\n",
                     "Задание 4. Ввести большое целое число и получить цифру, наибольшую из введенных\n",
                     "Задание 5. Ввести значения прибыли и издержек, чтобы получить баланс\n",
                     "Задание 6. Введите значения: сколько пробегает бегун каждый день? "
                     "Должен пробежать не менее скольки километров?\n"]
    status_input_function(input_message[0])
    status_input_function(input_message[1])
    sec_to_time(input_message[2])
    max_number(input_message[3])
    my_firm(input_message[4])
    runner(input_message[5])


if __name__ == '__main__':
    main()
