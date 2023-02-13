import sys
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog
from Dialogo_seleccion_pais import *


class Dialog_SeleccionPais_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog_SeleccionPais()
        self.ui.setupUi(self)

        self.paises = ('Argentuna', 'Brazil', 'Colombia', 'Ecuador','Guatemala', 'Perú', 'Mexico', 'Urguay')

        self.ui.btn_seleccionar_pais.clicked.connect(self.mostrar_paises)

        self.show()

    def mostrar_paises(self):
        pais, estado = QInputDialog.getItem(self, 'Seleccion Pais', 'Selecciona sus país', self.paises, 5, True)

        if estado and pais:
            self.ui.txt_pais.setText(pais)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialog_SeleccionPais_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
