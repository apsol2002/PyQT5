import sys
from PyQt5.QtWidgets import QApplication, QDialog
from DialogoTiendaInformatica import *


class DialogoTiendaInformatica_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_DialogoTiendaInformatica()
        self.ui.setupUi(self)

        self.ui.sbx_mouse.editingFinished.connect(self.calcular_precio)
        self.ui.sbx_teclado.editingFinished.connect(self.calcular_precio)


    def calcular_precio(self):
        teclados = self.ui.sbx_teclado.value()
        mouses = self.ui.sbx_mouse.value()

        precio_teclado = int(self.ui.txt_teclado.text())
        mensaje_teclado = f'Por {teclados} teclados debes pagar {(teclados*precio_teclado)}'
        self.ui.txt_subtotal_1.setText(str(teclados*precio_teclado))


        self.ui.lbl_muestra_total.setText(mensaje_teclado)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = DialogoTiendaInformatica_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
