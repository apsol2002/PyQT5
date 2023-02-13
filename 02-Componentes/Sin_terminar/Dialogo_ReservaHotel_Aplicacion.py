import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from Dialogo_ReservaHotel import *


class Dialogo_ReservaHotel_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_DialogoReservaHotel()
        self.ui.setupUi(self)

        self.ui.btn_calcular_costo.clicked.connect(self.calcular_costo)
        self.ui.btn_reservar_y_mostrar.clicked.connect(self.mostrar_reserva)

    def calcular_costo(self):

        precio = 0
        precio_tipo_habitacion = 0
        precio_mascota = 0

        fecha = self.ui.cal_calendario.selectedDate()
        dia_actual = fecha.day()
        dia_de_la_semana = fecha.dayOfWeek()

        cantidad_dias = int(self.ui.sbx_cantidad_dias.value())

        tipo_habitacion = self.ui.cbx_tipo_habitacion.currentText()
        if tipo_habitacion == 'Simple':
            precio_tipo_habitacion = 1500
        if tipo_habitacion == 'Doble':
            precio_tipo_habitacion = 2500
        if tipo_habitacion == 'Penhouse':
            precio_tipo_habitacion = 4500

        mascotas = self.ui.chk_mascota.isChecked()
        if mascotas:
            precio_mascota += 800

        lista_tipo_dias = self.generar_lista_tipo_dias(dia_de_la_semana, cantidad_dias)

        for d in lista_tipo_dias:
            precio += (precio_tipo_habitacion * d) + precio_mascota

        self.ui.lbl_mostrar_total.setText(str(precio))

    def mostrar_reserva(self):
        print('mostrar_reserva')

    def generar_lista_tipo_dias(self, dia, cantidad):

        lista = []

        for d in range(dia, (dia + cantidad)):

            if d > 28:
                d -= 28
            elif d > 21:
                d -= 21
            elif d > 14:
                d -= 14
            elif d > 7:
                d -= 7

            if d in range(6):
                lista.append(1)
            else:
                lista.append(2)

        return lista

    def calcular_dia_semana(self, actual):

        dia = ''

        if actual - 1 == 0:
            dia = 'Lunes'
        elif actual - 1 == 1:
            dia = 'Martes'
        elif actual - 1 == 2:
            dia = 'Miércoles'
        elif actual - 1 == 3:
            dia = 'Jueves'
        elif actual - 1 == 4:
            dia = 'Viernes'
        elif actual - 1 == 5:
            dia = 'Sabado'
        elif actual - 1 == 6:
            dia = 'Domingo'

        return dia


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_ReservaHotel_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
