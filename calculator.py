import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton

class CalculatorWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.MyUI()

    def MyUI(self):
        grid = QGridLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        grid.addWidget(self.display, 0, 0, 1, 4)

        names = ['7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '=', 'с', '+']

        positions = [(i, j) for i in range(1, 5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '=':
                btn = QPushButton(name)
                btn.clicked.connect(self.equals)
                grid.addWidget(btn, *position)
            elif name == "с":
                btn = QPushButton(name)
                btn.clicked.connect(self.reset)
                grid.addWidget(btn, *position)
            else:
                btn = QPushButton(name)
                btn.clicked.connect(lambda x, b=name: self.append_number(b))
                grid.addWidget(btn, *position)

        self.setLayout(grid)
        self.setWindowTitle('Nizom Calculator')

    def reset(self):
        self.display.setText("")

    def append_number(self, b):
        self.display.setText(self.display.text() + b)

    def equals(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except:
            self.display.setText('Error')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    calculator.show()
    sys.exit(app.exec())
