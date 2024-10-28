import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QGridLayout, QLineEdit, QAction
from PyQt5.QtGui import QIcon

class GridExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadmenu()

    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        grid = QGridLayout()
        centralWidget.setLayout(grid)

        names = ['7', '8', '9', '/', 'sin',
                 '4', '5', '6', '*', 'cos',
                 '1', '2', '3', '-', '**',
                 '0', '.', '=', '+', 'Save',
                 '', '', '', '', '']

        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 1, 1, 5)

        positions = [(i, j) for i in range(1, 6) for j in range(1, 6)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon("calculator"))
        self.show()

    def loadmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')

        exitButton = QAction('Exit', self)
        exitButton.setShortcut("ctrl+Q")
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridExample()
    sys.exit(app.exec_())