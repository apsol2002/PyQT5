import sys
import sqlite3
from sqlite3 import Error as db_error
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
import re
import os
from Dialogo_InsercionDatosBD import *


class Dialogo_InsercionDatosBD_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialogo_InsercionDatosBD()
        self.ui.setupUi(self)

        patron = '[a-zA-Z]+'
        self.regex = re.compile(patron)

        patron = '[1-9]{1}[0-9]*'
        self.regex_id_valido = re.compile(patron)

        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Mensajes")

        self.conexion = None

        self.ui.btn_conectar.clicked.connect(self.conectar)
        self.ui.btn_insertar_registro.clicked.connect(self.insertar)

        self.ui.txt_nombre_tabla.setEnabled(False)
        self.ui.txt_id.setEnabled(False)
        self.ui.txt_nombre.setEnabled(False)
        self.ui.btn_insertar_registro.setEnabled(False)

        self.show()

    def conectar(self):
        nombre_base = self.ui.txt_nombre_base_datos.text().strip()

        if self.regex.match(nombre_base) is not None:
            nombre_base = nombre_base + '.db'
            if os.path.exists(nombre_base):
                try:
                    self.conexion = sqlite3.connect(nombre_base)

                    self.mensaje.setText('Conexion a la base de datos satisfactoria.')
                    self.mensaje.setIcon(QMessageBox.Information)
                    self.mensaje.exec_()

                    self.ui.txt_nombre_tabla.setEnabled(True)
                    self.ui.txt_id.setEnabled(True)
                    self.ui.txt_nombre.setEnabled(True)
                    self.ui.btn_insertar_registro.setEnabled(True)

                    self.ui.txt_nombre_base_datos.setEnabled(False)
                    self.ui.btn_conectar.setEnabled(False)

                except db_error:
                    self.mensaje.setText('No se pudo conectar con {} .'.format(nombre_base) +
                                         '\n' + db_error.sqlite_errorname)
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.exec_()
            else:
                self.mensaje.setText('No existe la base de datos {} .'.format(nombre_base))
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.exec_()
        else:
            self.mensaje.setText('Escribe un nombre de DB válido')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()

    def insertar(self):
        nombre_tabla = self.ui.txt_nombre_tabla.text().strip()

        if self.regex.match(nombre_tabla) is not None:

            valor_id = self.ui.txt_id.text().strip()

            if self.regex_id_valido.match(valor_id) is not None:

                if not self.existe_id(nombre_tabla,valor_id):

                    nombre_producto = self.ui.txt_nombre.text().strip()

                    if self.regex.match(nombre_producto) is not None:

                        try:
                            sql = '''INSERT INTO {} (id, nombre) VALUES ({}, "{}")'''.format(nombre_tabla, valor_id, nombre_producto)

                            cursor = self.conexion.cursor()
                            self.conexion.commit()
                            cursor.execute(sql)

                            self.mensaje.setText('Registro ingresado de forma satisfactoria.')
                            self.mensaje.setIcon(QMessageBox.Information)
                            self.mensaje.exec_()

                            self.ui.txt_nombre.setText('')

                        except db_error as e:
                            print('El ´problema es: ' + e.sqlite_errorname.__str__())
                    else:
                        self.mensaje.setText('Debe ingresar un nombre de producto válido ')
                        self.mensaje.setIcon(QMessageBox.Warning)
                        self.mensaje.exec_()
                else:
                    self.mensaje.setText('El ID especificado ya existe.. ')
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.exec_()
            else:
                self.mensaje.setText('Escribe un numero de ID valido ')
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.exec_()
        else:
            self.mensaje.setText('Escribe un nombre de tabla')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()

    def existe_id(self, tabla, valor_id):
        sql = '''SELECT * FROM {} WHERE ID = {}'''.format(tabla,valor_id)
        cursor = self.conexion.cursor()
        resultado = cursor.execute(sql).fetchall()

        return len(resultado) > 0



if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_InsercionDatosBD_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
