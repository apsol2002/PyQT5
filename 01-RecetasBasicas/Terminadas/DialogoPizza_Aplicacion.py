import sys
from PyQt5.QtWidgets import QApplication,QDialog
from DialogoPizza import DialogPizza

class DialogoPizza_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = DialogPizza()
        self.ui.setupUi(self)

        self.ui.chk_queso.stateChanged.connect(self.calcular_precio)
        self.ui.chk_aceitunas.stateChanged.connect(self.calcular_precio)
        self.ui.chk_salsas.stateChanged.connect(self.calcular_precio)


    def calcular_precio(self):
        pizza = 150

        if self.ui.chk_queso.isChecked() == True:
            pizza += 45

        if self.ui.chk_aceitunas.isChecked() == True:
            pizza += 30

        if self.ui.chk_salsas.isChecked() == True:
            pizza += 55

        self.ui.label_3.setText(f'El precio a pagar es de {pizza} pesos ')

        coords = self.ui.lbl_precio_pizza.geometry().getCoords()
        print(coords[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = DialogoPizza_Aplicacion()
    dialogo.show()

    app.exec(app.exec_())
