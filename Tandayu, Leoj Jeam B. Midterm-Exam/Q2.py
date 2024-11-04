import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP"
        self.x = 200
        self.y = 200
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x , self.y , self.width, self.height)
        self.setWindowIcon(QIcon('feather'))

        self.button = QPushButton('Click To Change Color', self)
        self.button.move(190, 190)
        self.button.clicked.connect(self.change_color)
        self.show()

    def change_color(self, win):
        self.button.setStyleSheet('background-color: yellow')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


