import sys
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from Dialogo_ConsultaDatosTabla import *
import re,os


class Dialogo_ConsultaDatosTabla_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialogo_ConsultaDatosTabla()
        self.ui.setupUi(self)

        patron = '[a-zA-Z]+'
        self.validador = re.compile(patron)

        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_consultar_datos.clicked.connect(self.consultar_datos)

    def consultar_datos(self):
        nombre_bd = self.ui.txt_nombre_base_datos.text().strip()

        if self.validador.match(nombre_bd) is not None:

            nombre_bd = nombre_bd + '.db'
            if os.path.exists(nombre_bd):
                nombre_tabla = self.ui.txt_nombre_tabla.text().strip()
                if self.validador.match(nombre_tabla) is not None:
                    try:

                        sql = '''SELECT * FROM {}'''.format(nombre_tabla)
                        conxion = sqlite3.connect(nombre_bd)
                        cur = conxion.cursor()
                        productos = cur.execute(sql).fetchall()

                        if len(productos) > 0:

                            fila = 0
                            for p in productos:
                                columna = 0
                                for c in p:
                                    celda = QTableWidgetItem(str(c)) # sería mejor dicho cada VALOR
                                    self.ui.tbl_datos.setItem(fila,columna,celda)
                                    columna +=1
                                fila += 1

                        else:
                            self.mensaje.setText('La tabla está vacía.')
                            self.mensaje.setIcon(QMessageBox.Warning)
                            self.mensaje.exec_()
                    except Error as e:
                        self.mensaje.setText('Error al conectar a la base de datos..')
                        self.mensaje.setIcon(QMessageBox.Warning)
                        self.mensaje.exec_()
                        print(e.sqlite_errorname + 'PUTA MADRE')
                    finally:
                        conxion.close()
                else:
                    self.mensaje.setText('El nombre de la TABLA no es valido')
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.exec_()
            else:
                self.mensaje.setText('no hay una BASE DE DATOS con ese nombre ')
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.exec_()
        else:
            self.mensaje.setText('El nombre de la BASE DE DATOS no es valido')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_ConsultaDatosTabla_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
