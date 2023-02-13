import sys
import Dialogo1
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Dialogo1.Dialogo1
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
