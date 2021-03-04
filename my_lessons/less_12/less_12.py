"""
1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито,year': 2014}]}
С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал. Записать
результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них
информацию. И получить объект: словарь из предыдущего задания.
"""
import pickle
import json

my_favourite_group = {'name': 'Г.М.О.', 'tracks': ['Последний месяц осени', 'Шапито'],
                      'Albums': [{'name': 'Делать панк-рок', 'year': 2016}, {'name': 'Шапито', 'year': 2014}]}


def get_serial():
    pic_data = pickle.dumps(my_favourite_group)
    js_dta = json.dumps(my_favourite_group).encode('utf-8')
    print(pic_data)
    print(js_dta.decode(encoding='UTF-8'))
    with open('pic_data.pickle', 'wb') as fp:
        pickle.dump(my_favourite_group, fp)

    with open('js_data.json', 'w', encoding='UTF-8') as fs:
        json.dump(my_favourite_group, fs)


get_serial()


def deserial():
    with open('pic_data.pkl', 'rb') as fp:
        resultp = pickle.load(fp)
        print(resultp)

    with open('js_data.json', 'r', encoding='UTF-8') as fs:
        resultf = json.load(fs)
        print(resultf)


deserial()
