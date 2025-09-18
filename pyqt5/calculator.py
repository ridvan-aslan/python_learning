import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator App")
        self.setGeometry(300, 300, 400, 400)
        self.setToolTip("This is a Calculator")
        self.init_UI()

    def init_UI(self):
        
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("Number 1")
        self.lbl_num1.move(50, 30)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Number 2")
        self.lbl_num2.move(50, 70)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(120, 30)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(120, 70)


        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("Add")
        self.btn_add.move(50, 110)
        self.btn_add.clicked.connect(self.calculate)

        self.btn_subtract = QtWidgets.QPushButton(self)
        self.btn_subtract.setText("Subtract")
        self.btn_subtract.move(50, 150)
        self.btn_subtract.clicked.connect(self.calculate)

        self.btn_multiply = QtWidgets.QPushButton(self)
        self.btn_multiply.setText("Multiply")
        self.btn_multiply.move(50, 190)
        self.btn_multiply.clicked.connect(self.calculate)

        self.btn_divide = QtWidgets.QPushButton(self)
        self.btn_divide.setText("Divide")
        self.btn_divide.move(50, 230)
        self.btn_divide.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(200, 50)
        self.lbl_result.move(50, 270)

    def calculate(self):
        num1 = int(self.txt_num1.text())
        num2 = int(self.txt_num2.text())
        
        if self.sender().text() == "Add":
            result = num1 + num2
        elif self.sender().text() == "Subtract":
            result = num1 - num2
        elif self.sender().text() == "Multiply":
            result = num1 * num2
        elif self.sender().text() == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                self.lbl_result.setText("Error: Division by zero")
                return


        self.lbl_result.setText("Result: " + str(result))


def window():
    app = QApplication(sys.argv)
    win = MyForm()
    win.show()
    sys.exit(app.exec_())

window()

