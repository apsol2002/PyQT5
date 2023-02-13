import sys
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from Dialogo_BusquedaDatos import *
import re



class Dialogo_BusquedaDatos_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialogo_BusquedaDatos()
        self.ui.setupUi(self)

        patron = '[1-9][0-9]+'
        self.validador = re.compile(patron)

        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_buscar.clicked.connect(self.buscar_producto_por_id)

        self.show()

    def buscar_producto_por_id(self):
        id_producto = self.ui.txt_id.text().strip()

        if self.validador.match(id_producto) is not None:
            try:
                conexion = sqlite3.connect('../clientes.db')

                sql = '''SELECT id, nombre FROM productos WHERE id = ?'''

                cur = conexion.cursor()

                producto = cur.execute(sql, (id_producto,)).fetchall()

                if len(producto)>0:
                    self.ui.txt_nombre.setText(producto[0][1])
                else:
                    self.mensaje.setText('No hay productos para el ID asociado ...')
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.show()

            except Error as e:
                self.mensaje.setText('Error al conectar a la BASE DE DATOS ... ')
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.show()
        else:
            self.mensaje.setText('El ID no es valido')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_BusquedaDatos_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
