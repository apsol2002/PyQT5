import sys
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from Dialogo_CreacionTabla import *
from collections import namedtuple
import re


Columna = namedtuple('Columna', ['nombre', 'tipo'])

class Dialogo_CreacionTabla_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialogo_CreacionTabla()
        self.ui.setupUi(self)

        self.columnas = []
        patron = '[a-zA-Z]+'
        self.regexp = re.compile(patron)
        self.mensajes = QMessageBox(self)

        self.ui.btn_abgregar_columna.clicked.connect(self.agregar_columna)
        self.ui.btn_crear_base_datos.clicked.connect(self.crear_base_datos)

        self.show()

    def agregar_columna(self):

        nombre_columna = self.ui.txt_nombre_columna.text().strip() #strip limpia de espacios _*_

        if self.regexp.match(nombre_columna) is not None: # None / MatchObject
            # tipo_columna = self.ui.cbx_tipo_dato.itemText(self.ui.cbx_tipo_dato.currentIndex())

            tipo_columna = str(self.ui.cbx_tipo_dato.currentText())
            self.columnas.append(Columna(nombre_columna,tipo_columna))

            self.ui.lbl_resultados.setText('Columna {} agregada con éxito'.format(str(len(self.columnas))))

        else:
            self.mensajes.setWindowTitle('Mensaje')
            self.mensajes.setText('Escribe un nombre de columna valido \n Solo caracteres alfanuméricos..')
            self.mensajes.exec_()


    def crear_base_datos(self):
        nombre_base_datos = self.ui.txt_nombre_base_datos.text().strip()
        nombre_tabla = self.ui.txt_nombre_tabla.text().strip()

        if self.regexp.match(nombre_base_datos) is not None:
            if self.regexp.match(nombre_tabla) is not None:

                if len(self.columnas) > 0:
                    sql = f'CREATE TABLE {nombre_tabla}('

                    plantilla_campos = '{} {}'
                    campos = []

                    for c in self.columnas:
                        campos.append(plantilla_campos.format(c.nombre, c.tipo))

                    lista_campos = ','.join(campos)

                    sql += lista_campos + ')'

                    print(sql)

                    try:
                        conexion = sqlite3.connect(f'{nombre_base_datos}.db')

                        cursor = conexion.cursor()
                        cursor.execute(sql)
                        conexion.commit()

                        self.ui.lbl_resultados.setText('Base y Tabla creadas con éxito.')


                    except Error as e:
                        self.mensajes.setIcon(QMessageBox.Warning)
                        self.mensajes.setWindowTitle('Mensaje')
                        self.mensajes.setText('Error al crear la base de datos.')
                        self.mensajes.exec_()
                    finally:
                        conexion.close()

                else:
                    self.mensajes.setWindowTitle('Mensaje')
                    self.mensajes.setText('Debe ingresar a menos una columna.')
                    self.mensajes.exec_()

            else:
                self.mensajes.setWindowTitle('Mensaje')
                self.mensajes.setText('Debe escribir un nombre de Tabla valido \n Solo caracteres alfanuméricos..')
                self.mensajes.exec_()
        else:
            self.mensajes.setWindowTitle('Mensaje')
            self.mensajes.setText('Debe escribir un nombre de Base de Datos \n Solo caracteres alfanuméricos..')
            self.mensajes.exec_()

        for c in self.columnas:
            print(c)
        print(f'Hay un total de: {str(len(self.columnas))}')



if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_CreacionTabla_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
