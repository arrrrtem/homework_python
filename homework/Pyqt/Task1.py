"""
С помощью Pyqt создайте калькулятор с графическим интерфейсом.
Приложение должно выполнять: Сложение, вычитание, деление, умножение, возведение в степень, запоминание значения,
вывод значения из памяти.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.memory_value = 0  # Переменная для хранения значения в памяти

        # Создаем поле ввода
        self.display = QLineEdit(self)
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)

        # Создаем кнопки
        self.create_button("7")
        self.create_button("8")
        self.create_button("9")
        self.create_button("/")
        self.create_button("4")
        self.create_button("5")
        self.create_button("6")
        self.create_button("*")
        self.create_button("1")
        self.create_button("2")
        self.create_button("3")
        self.create_button("-")
        self.create_button("0")
        self.create_button(".")
        self.create_button("=")
        self.create_button("+")
        self.create_button("C", self.clear_display)
        self.create_button("M+", self.memory_add)
        self.create_button("MR", self.memory_recall)

        # Создаем основной макет
        layout = QVBoxLayout()
        layout.addWidget(self.display)

        # Группируем кнопки по 4 в ряд
        for i in range(0, len(self.buttons), 4):
            button_row = self.buttons[i:i+4]
            button_row_layout = QHBoxLayout()
            for button in button_row:
                button_row_layout.addWidget(button)
            layout.addLayout(button_row_layout)

        self.setLayout(layout)

    def create_button(self, text, click_function=None):
        button = QPushButton(text, self)
        button.clicked.connect(lambda: self.on_button_click(text, click_function))
        self.buttons.append(button)

    def on_button_click(self, button_text, click_function):
        if click_function:
            click_function()
        else:
            current_text = self.display.text()
            new_text = current_text + button_text
            self.display.setText(new_text)

    def clear_display(self):
        self.display.clear()

    def memory_add(self):
        try:
            value = float(self.display.text())
            self.memory_value += value
            self.clear_display()
        except ValueError:
            pass

    def memory_recall(self):
        self.display.setText(str(self.memory_value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.setWindowTitle("Simple Calculator")
    calculator.setGeometry(100, 100, 300, 400)
    calculator.show()
    sys.exit(app.exec())
