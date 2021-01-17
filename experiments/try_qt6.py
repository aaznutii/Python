# Импортируется библиотека PyQt6 для показа красивых окон
from PyQt6.QtWidgets import *

# Переменные c названиями кнопок в виде массивов, итоговые сообщения, словарь функций
task_text = ['Введите число для демонстрации', 'Введите текст для демонстрации']
btn_text = ['Показать занчение переменной', 'Показать занчение переменной',
            'Рассчитать значение времени', 'Рассчитать число по формуле:', '']
answer_text = ['Вы ввели число:', 'Вы ввели строку:', 'Вы указали в секндах ровно:',
               'По формуле получается следующая сумма:', 'Самая большая цифра в числе:',
               ['Прибыль', 'Убыток'], ['Рентабельность составила', 'Прибыль на 1-го сотрудника составила:'],
               ['На ', '', '']]
function_list = {}


# Создается пользовательский класс для работы с красивыми окнами, куда вносятся кнопки и поля ввода
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit(str(task_text[0]))
        self.button_check = QPushButton(btn_text[0])
        self.button_check.clicked.connect(self.on_check)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button_check)

        self.setLayout(layout)

    def on_check(self):
        text = self.line_edit.text()

        try:
            value = int(text)
            QMessageBox.information(self, 'Информация', 'Введено число: "{}"'.format(value))
        except:
            QMessageBox.information(self, 'Внимание', 'Введен текст: "{}"'.format(text))


# Условие дня начала работы всей программы
if __name__ == '__main__':
    app = QApplication([])

    mw = Window()
    mw.show()

    app.exec()
