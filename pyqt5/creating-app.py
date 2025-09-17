import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip

def window():
    app = QApplication(sys.argv)
    win = QMainWindow() 
    win.show()

    win.setWindowTitle("PyQt5 App")
    win.setGeometry(200, 200, 300, 300)
    win.setToolTip("This is a QMainWindow")
    

    sys.exit(app.exec_())


window()