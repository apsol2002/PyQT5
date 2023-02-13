import sys
from PyQt5.QtWidgets import QApplication,QDialog
from DialogoVentaCamisa import DialogoVentaCamisa

class DialogoVentaCamisa_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = DialogoVentaCamisa()
        self.ui.setupUi(self)

        self.ui.rbn_talla_l.toggled.connect(self.mostrar_talle_y_pago)
        self.ui.rbn_talla_m.toggled.connect(self.mostrar_talle_y_pago)
        self.ui.rbn_talla_xl.toggled.connect(self.mostrar_talle_y_pago)
        self.ui.rbn_talla_xxl.toggled.connect(self.mostrar_talle_y_pago)

        self.ui.rbn_contraentrega.toggled.connect(self.mostrar_talle_y_pago)
        self.ui.rbn_tarjeta_debito_credito.toggled.connect(self.mostrar_talle_y_pago)
        self.ui.rbn_consignacion_bancaria.toggled.connect(self.mostrar_talle_y_pago)

    def mostrar_talle_y_pago(self):
        talle = ''
        forma_pago = ''

        if self.ui.rbn_talla_l.isChecked() == True:
            talle = 'L'

        if self.ui.rbn_talla_m.isChecked() == True:
            talle = 'M'

        if self.ui.rbn_talla_xl.isChecked() == True:
            talle = 'XL'

        if self.ui.rbn_talla_xxl.isChecked() == True:
            talle = 'XXL'


        if self.ui.rbn_tarjeta_debito_credito.isChecked() == True:
            forma_pago = 'Tarj Deb/Credito'

        if self.ui.rbn_contraentrega.isChecked() == True:
            forma_pago = 'Contraentrega'

        if self.ui.rbn_consignacion_bancaria.isChecked() == True:
            forma_pago = 'Consignacion Bancaria'

        mensaje = 'El talle es {} y la forma de pago es {}'.format(talle,forma_pago)
        self.ui.lbl_mostrar_resultado.setText(mensaje)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = DialogoVentaCamisa_Aplicacion()
    dialogo.show()

    app.exit(app.exec_())

