import sys
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from DialogoCreacionBaseDeDatos import *


class DialogoCreacionBaseDeDatos_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_DialogoCreacionBaseDeDatos()
        self.ui.setupUi(self)

        self.ui.btn_crear_base_datos.clicked.connect(self.crear_base_datos)

    def crear_base_datos(self):

        nombre_base_datos = self.ui.txt_nombre_base_datos.text()

        if len(nombre_base_datos) > 0:

            try:
                conexion = sqlite3.connect('{}.db'.format(nombre_base_datos))
                self.ui.lbl_resultado.setText('Base de datos creada con exito')
            except Error as e:
                self.ui.lbl_resultado.setText('Ha ocurrido un error', e.sqlite_errorname)
            finally:
                conexion.close()

        else:
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setWindowTitle('Mensaje de error')
            mensaje.setText('Debe escribir un nombre')
            mensaje.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = DialogoCreacionBaseDeDatos_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
