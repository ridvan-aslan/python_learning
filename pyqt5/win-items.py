import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 App")
        self.setGeometry(200, 200, 300, 300)
        self.setToolTip("This is a QMainWindow")
        self.init_UI()


    def init_UI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Name")
        self.lbl_name.move(50, 30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Surname")
        self.lbl_surname.move(50, 70)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(120, 30)
        
        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(120, 70)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(200, 50)
        self.lbl_result.move(120, 150)
 
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(120, 110)
        self.btn_save.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        lbl_result = self.lbl_result
        txt_name = self.txt_name.text()
        txt_surname = self.txt_surname.text()
        lbl_result.setText("Hello " + txt_name + " " + txt_surname)

        
def window():
    app = QApplication(sys.argv)
    win = MyWindow() 
    win.show()
    sys.exit(app.exec_())

window()