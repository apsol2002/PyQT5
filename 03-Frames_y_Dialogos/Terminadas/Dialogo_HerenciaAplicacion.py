import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtGui import QIcon

class Aplicacion(QMainWindow):
    def __init__(self):
        super(Aplicacion, self).__init__()

        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle('Jerarquía de Herencia')
        # self.setWindowIcon(QIcon('archivo.ico'))

                                #  texto   , componente padre
        btn_saludar = QPushButton('Saludar', self)
        btn_saludar.move(200,100)
        btn_saludar.clicked.connect(self.saludar)

        self.show()

    def saludar(self):
        mensaje = QMessageBox()
        mensaje.setText('Bienventido a PyQt5 ')
        mensaje.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
