import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QPushButton
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "PyQT Button"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x , self.y , self.width , self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.button = QPushButton('Click Me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(110,70)

        self.button_1 = QPushButton('Register!', self)
        self.button_1.setToolTip("this button does nothing.. yet.")
        self.button_1.move(110, 100)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())