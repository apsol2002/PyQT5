import sys
from PyQt5.QtWidgets import QApplication, QDialog
from Dialogo_restaurante import *


class Dialogo_restaurante_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialogo_restaurante()
        self.ui.setupUi(self)

    def funcion(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_restaurante_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
