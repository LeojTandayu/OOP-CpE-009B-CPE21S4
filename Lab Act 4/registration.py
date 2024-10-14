import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Register"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('person'))

        self.textboxlbl = QLabel("Sign Up", self)
        self.textboxlbl.move(130,25)

        self.textboxlbl1 = QLabel("First Name :", self)
        self.textboxlbl1.move(30,60)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(100,58)
        self.textbox1.resize(150,20)

        self.textboxlbl2 = QLabel("Last Name :", self)
        self.textboxlbl2.move(30, 90)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(100, 88)
        self.textbox2.resize(150, 20)

        self.textboxlbl3 = QLabel("Username :", self)
        self.textboxlbl3.move(30, 120)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(100, 118)
        self.textbox3.resize(150, 20)

        self.textboxlbl4 = QLabel("Password :", self)
        self.textboxlbl4.move(30, 150)
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(100, 148)
        self.textbox4.resize(150, 20)

        self.textboxlbl5 = QLabel("Email:", self)
        self.textboxlbl5.move(30, 180)
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(100, 178)
        self.textbox5.resize(150, 20)

        self.textboxlbl6 = QLabel("Contact Number :", self)
        self.textboxlbl6.move(30, 210)
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(120, 208)
        self.textbox6.resize(130, 20)

        self.submitButton = QPushButton("Submit", self)
        self.submitButton.move(50, 250)
        self.submitButton.clicked.connect(self.save_account_details)

        self.clearButton = QPushButton("Clear", self)
        self.clearButton.move(160, 250)
        self.clearButton.clicked.connect(self.clear_fields)


        self.show()

    def save_account_details(self):
        info = [
            self.textbox1.text(),
            self.textbox2.text(),
            self.textbox3.text(),
            self.textbox4.text(),
            self.textbox5.text(),
            self.textbox6.text()
        ]

        # Check if all fields are filled
        if any(not info for info in info):
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        with open('account_details.txt', 'a') as f:
            f.write(', '.join(info) + '\n')
        QMessageBox.information(self, "Success", "Details Saved Successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.textbox1.clear()
        self.textbox2.clear()
        self.textbox3.clear()
        self.textbox4.clear()
        self.textbox5.clear()
        self.textbox6.clear()
        QMessageBox.information(self, "Cleared", "Cleared Successfully!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())