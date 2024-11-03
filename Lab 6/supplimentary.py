import sys
import math
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QGridLayout, QLineEdit, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadMenu()

    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        grid = QGridLayout()
        centralWidget.setLayout(grid)

        names = ['7', '8', '9', '/', 'sin',
                 '4', '5', '6', '*', 'cos',
                 '1', '2', '3', '-', '**',
                 '0', '.', '=', '+', 'Save',
                 'C', '(', ')', '', '']

        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 1, 1, 5)

        positions = [(i, j) for i in range(1, 6) for j in range(1, 6)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, *position)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon("calculator"))
        self.show()

    def loadMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')

        exitButton = QAction('Exit', self)
        exitButton.setShortcut("ctrl+Q")
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        loadButton = QAction('Load', self)
        loadButton.triggered.connect(self.load_from_file)
        fileMenu.addAction(loadButton)

    def on_button_click(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            try:
                expression = self.textLine.text()
                expression = expression.replace('sin(', 'math.sin(math.radians(')
                expression = expression.replace('cos(', 'math.cos(math.radians(')

                open_parentheses = expression.count('(')
                close_parentheses = expression.count(')')
                if open_parentheses > close_parentheses:
                    expression += ')' * (open_parentheses - close_parentheses)

                result = eval(expression)

                self.textLine.setText(f"{result:.4f}")
                self.save_operation(self.textLine.text())
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Invalid input: ')
        elif button_text == 'C':
            self.textLine.clear()
        else:
            current_text = self.textLine.text()
            self.textLine.setText(current_text + button_text)

    def save_operation(self, operation):
        with open('history.txt', 'a') as f:
            f.write(operation + '\n')

    def load_from_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as f:
                content = f.read()
                self.textLine.setText(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
