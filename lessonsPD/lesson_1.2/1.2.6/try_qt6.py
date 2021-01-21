"""
Основной исполняемый файл. Курс 1., урок 2., задание *6.
Для начала работы исполните файл.
Как понимаю, для корректной работы необходима библиотека PyQt6
Данные о товарах вносятся в файл lists.txt
Днные для анализа вносятся в файл for_analysis.txt
Не все получилось, что хотел, но все работает.
"""
# Импортируется библиотека PyQt6 для показа красивых окон
from PyQt6.QtWidgets import *
# Импорт файла с основными функциями
import mean


# Создается пользовательский класс для работы с красивыми окнами, куда вносятся кнопки и поля ввода
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Введение полей
        self.label = QLabel('Ввести товар')
        self.line_edit_name = QLineEdit('Название товара')
        self.line_edit_price = QLineEdit('Цена')
        self.line_edit_count = QLineEdit('Количество')
        self.line_edit_units = QLineEdit('Ед.измерения')
        self.button_check = QPushButton('Добавить товар')
        self.button_check.clicked.connect(self.on_check)
        self.btn_analytics = QPushButton('Генерировать аналитику')
        self.btn_analytics.clicked.connect(self.get_analytics)
        # Показать поля
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit_name)
        layout.addWidget(self.line_edit_price)
        layout.addWidget(self.line_edit_count)
        layout.addWidget(self.line_edit_units)
        layout.addWidget(self.button_check)
        layout.addWidget(self.btn_analytics)

        self.setLayout(layout)

    # При нажатии кнопки "Дабавить товар"
    def on_check(self):
        name = mean.input_value(self.line_edit_name.text())
        price = mean.input_value(self.line_edit_price.text())
        count = mean.input_value(self.line_edit_count.text())
        units = mean.input_value(self.line_edit_units.text())

        number = mean.count_for_products()
        new_product = str((number, {'name': name, 'price': price, 'count': count, 'units': units}))  # строка
        mean.append_lists(new_product, 'lists.txt')  # запись
        QMessageBox.information(self, 'Информация', 'Сохранены следующие данные:\n'  # контроль
                                                    f'name: {name}\n'
                                                    f'price: {price}\n'
                                                    f'count: {count}\n'
                                                    f'units: {units}\n'
                                                    f'Индекс записи: {number}')

    def get_analytics(self):
        mean.create_analytics_dict()
        QMessageBox.information(self, 'Информация', 'Значения сохранены в файл:\n for_analysis.txt')


# Условие дня начала работы всей программы
if __name__ == '__main__':
    app = QApplication([])

    mw = Window()
    mw.show()

    app.exec()
