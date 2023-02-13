import sys
from PyQt5.QtWidgets import QApplication, QDialog
from DialogoHeladerias import Ui_DialogoHeladera

class DialogoHeladera_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_DialogoHeladera()
        self.ui.setupUi(self)

        self.ui.chk_chocolate.stateChanged.connect(self.calcular_precio)
        self.ui.chk_frutilla.stateChanged.connect(self.calcular_precio)
        self.ui.chk_crema.stateChanged.connect(self.calcular_precio)


    def calcular_precio(self):
        precio = 0

        if self.ui.chk_chocolate.isChecked() == True:
            precio += 80

        if self.ui.chk_frutilla.isChecked() == True:
            precio += 80

        if self.ui.chk_crema.isChecked() == True:
            precio += 80

        print('El precio es: {} '.format(precio))
        print('El nombre de objeto de del chk_frutilla es:{}'.format(str(self.ui.chk_frutilla.objectName())))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = DialogoHeladera_Aplicacion()
    dialogo.show()

    app.exec(app.exec_())


