import sys
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from Dialogo_NavegacionRegistros import *


class Dialogo_NavegacionRegistros_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.total_registros = 0
        self.registro = 1

        self.ui = Ui_Dialogo_NavegacionRegistros()
        self.ui.setupUi(self)

        self.ui.btn_primero.clicked.connect(self.primero)
        self.ui.btn_anterior.clicked.connect(self.anterior)
        self.ui.btn_siguiente.clicked.connect(self.siguiente)
        self.ui.btn_ultimo.clicked.connect(self.ultimo)

        self.conexion = None

        self.mensaje = QMessageBox()

        self.conectar_bd()

        self.primero()



    def conectar_bd(self):

        try:
            self.conexion = sqlite3.connect('../clientes.db')

            sql = '''SELECT * FROM productos'''
            cur = self.conexion.cursor()
            self.total_registros = len(cur.execute(sql).fetchall())

            # print(type(productos))

        except Error as e:
            self.mensaje.setText('Error al conectar con la base de datos \n {}'.format(e.sqlite_errorname))
            self.mensaje.setWindowTitle('Mensaje')
            self.exec_()
        finally:
            pass
            #self.conexion.close()

    def primero(self):

        sql = '''SELECT * FROM productos LIMIT 1'''
        cur = self.conexion.cursor()
        producto = cur.execute(sql).fetchone()

        if len(producto) > 0:
            self.ui.txt_id.setText(str(producto[0]))
            self.ui.txt_nombre.setText(producto[1])

        self.registro = 1

        '''     self.actual = 0

        producto = self.registros[0]

        self.ui.txt_id.setText('')
        self.ui.txt_nombre.setText('')

        self.ui.txt_id.setText(str(producto[0]))
        self.ui.txt_nombre.setText(producto[1])'''

    def anterior(self):
        if self.registro > 1:
            sql = '''SELECT * FROM productos ORDER BY id DESC LIMIT 1 OFFSET ?'''
            cur = self.conexion.cursor()

            self.registro -= 1

            producto = cur.execute(sql, (self.total_registros - self.registro,)).fetchone()

            if len(producto) > 0:
                self.ui.txt_id.setText(str(producto[0]))
                self.ui.txt_nombre.setText(producto[1])
        else:
            pass

    def siguiente(self):
        # sql = '''SELECT * FROM productos LIMIT 1 OFFSET {}'''.format(self.registro) FUNCIONA pero lo otro es nuevo ..

        if self.registro < self.total_registros:
            sql = '''SELECT * FROM productos LIMIT 1 OFFSET ?'''
            cur = self.conexion.cursor()
            producto = cur.execute(sql, (self.registro,)).fetchone()

            '''
            texto = '{} - {}'.format(self.registro, self.total_registros)

            mensaje = QMessageBox()
            mensaje.setText(texto)
            mensaje.exec_()'''

            self.registro += 1

            if len(producto) > 0:
                self.ui.txt_id.setText(str(producto[0]))
                self.ui.txt_nombre.setText(producto[1])
        else:
            pass

    def ultimo(self):
        sql = '''SELECT * FROM productos  ORDER BY id DESC LIMIT 1'''
        cur = self.conexion.cursor()
        producto = cur.execute(sql).fetchone()

        if len(producto) > 0:
            self.ui.txt_id.setText(str(producto[0]))
            self.ui.txt_nombre.setText(producto[1])

        self.registro = self.total_registros


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_NavegacionRegistros_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
