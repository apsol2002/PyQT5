import sys
from PyQt5.QtWidgets import QApplication, QDialog
from DialogoClaseVuelo import DialogoClaseVuelo


class DialogoClaseVuelo_Aplicacion(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = DialogoClaseVuelo()
        self.ui.setupUi(self)

        self.ui.rbn_primera_clase.toggled.connect(self.mostrar_informacion)
        self.ui.rbn_segunda_clase.toggled.connect(self.mostrar_informacion)
        self.ui.rbn_tercera_clase.toggled.connect(self.mostrar_informacion)

    def mostrar_informacion(self):
        costo_vuelo = 0

        if self.ui.rbn_primera_clase.isChecked() == True:
            costo_vuelo = 300
        if self.ui.rbn_segunda_clase.isChecked() == True:
            costo_vuelo = 200
        if self.ui.rbn_tercera_clase.isChecked() == True:
            costo_vuelo = 100

        mensaje = "El costo es de {} dólares".format(costo_vuelo)
        self.ui.lbl_resultado_seleccion.setText(mensaje)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = DialogoClaseVuelo_Aplicacion()
    dialogo.show()

    app.exit(app.exec_())
