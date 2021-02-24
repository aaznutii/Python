class First:
    def set_value(self, value):
        self.data = value

    def print_value(self):
        print(self.data)


l = [125, 55, 'ghhf', 'jghfh', ['jghf', 125]]

x = First()
y = First()
x.data = '5555'
y.data = 125

x.print_value()
y.print_value()

classlist = []
# создание экземпляров в цикле
for el in range(len(l)):
    i = el  # сохраняем индекс для работы со списком
    el = First()  # превращаем индекс в переменную - экземпляра класса
    el.data = l[i]  # присваиваем значение переменной экземпляра класса из списка
    el.print_value()
    classlist.append(el)  # Вносим все экземпляры в список

for el in classlist:
    print(el)
    el.print_value()
