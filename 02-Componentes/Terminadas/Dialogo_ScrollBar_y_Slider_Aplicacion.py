import sys
from PyQt5.QtWidgets import QApplication, QDialog
from Dialogo_ScrollBar_y_Slider import *


class Dialogo_ScrollBar_y_Slider_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialogo_ScrollBar_y_Slider()
        self.ui.setupUi(self)

        self.ui.horizontalScrollBar.valueChanged.connect(self.mostrar_valor)

    def mostrar_valor(self, valor):
        print(f'El valor del HorizontallScroll es{valor}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_ScrollBar_y_Slider_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
