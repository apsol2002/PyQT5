import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from Dialogo_InicioSesion import *
from passlib.hash import pbkdf2_sha256
import re
import sqlite3
from sqlite3 import Error

class Dialogo_InicioSesion_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialogo_InicioSesion()
        self.ui.setupUi(self)

        patron = r'[a-z0-9]+@+[a-z]+\.[a-z]+'
        self.validador = re.compile(patron)

        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

        self.show()

    def iniciar_sesion(self):
        correo = self.ui.txt_correo_electronico.text().strip()

        if len(correo) > 0 :

            if self.validador.match(correo) is not None:
                clave = self.ui.txt_contrasenia.text().strip()

                if len(clave) > 0:

                    try:

                        conexion = sqlite3.connect('../clientes.db')
                        cur = conexion.cursor()

                        sql = '''SELECT * FROM usuario WHERE correo = ?'''

                        usuario = cur.execute(sql, (correo,)).fetchone()
                        # print('El contenido de usuario es: ' + str(usuario))
                        if usuario is not None:

                            hash_almacenado = usuario[2]

                            if pbkdf2_sha256.verify(clave, hash_almacenado):
                                self.mensaje.setText("Ha iniciado sesion de forma satisfactoria.")
                                self.mensaje.exec_()
                            else:
                                self.mensaje.setText("La contraseña no es correcta.")
                                self.mensaje.exec_()

                        else:
                            self.mensaje.setText("No hay usuarios con ese CORREO")
                            self.mensaje.exec_()

                    except Error as e:
                        self.mensaje.setText("Error al conectar a la BASE DE DATOS ")
                        self.mensaje.exec_()

                else:
                    self.mensaje.setText("Debe escribir una CLAVE")
                    self.mensaje.exec_()

            else:
                self.mensaje.setText("el tipo de CORREO no es valido")
                self.mensaje.exec_()

        else:
            self.mensaje.setText("Debe escribir un correo electrónico")
            self.mensaje.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_InicioSesion_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
