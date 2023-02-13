import  sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoSaludo import *

class DialogoSaludoAplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.dialogo = Ui_Dialogo_saludar()
        self.dialogo.setupUi(self)

        self.dialogo.btn_saludar.clicked.connect(self.mostrar_saludo)
        self.show()

    def mostrar_saludo(self):
        nombre = self.dialogo.txt_nombre.text()
        self.dialogo.lbl_mensaje_saludo.setText(f"{nombre} este es un Hola Mundo PyQt5")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = DialogoSaludoAplicacion()
    dialogo.show()

    sys.exit(app.exec_())

