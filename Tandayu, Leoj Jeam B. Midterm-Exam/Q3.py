import sys
from logging import info

from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__ (self):
        super().__init__()
        self.title = "Midterm OOP"
        self.x = 200
        self.y = 200
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('feather'))

        self.textbox = QLineEdit(self)
        self.textbox.move(240,20)
        self.textbox.resize(240,20)


        self.textbox1 = QLabel("Enter your full name")
        self.textbox1.move(70 ,20)
        self.textbox1.resize(240, 20)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(240, 50)
        self.textbox2.resize(240, 20)

        self.button1 = QPushButton('Click to display your full name', self)
        self.button1.move(70 , 50)
        self.button1.clicked.connect(self.print)
        self.button1.setStyleSheet('color : red')
        self.show()

    def save_info(self):
        info = [self.textbox1.txt()]
    def print(self):
        print(info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())