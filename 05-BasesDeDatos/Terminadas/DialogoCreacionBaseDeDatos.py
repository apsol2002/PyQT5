# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoCreacionBaseDeDatos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogoCreacionBaseDeDatos(object):
    def setupUi(self, DialogoCreacionBaseDeDatos):
        DialogoCreacionBaseDeDatos.setObjectName("DialogoCreacionBaseDeDatos")
        DialogoCreacionBaseDeDatos.resize(479, 177)
        self.lbl_nombre_base_de_datos = QtWidgets.QLabel(DialogoCreacionBaseDeDatos)
        self.lbl_nombre_base_de_datos.setGeometry(QtCore.QRect(20, 40, 161, 30))
        self.lbl_nombre_base_de_datos.setObjectName("lbl_nombre_base_de_datos")
        self.txt_nombre_base_datos = QtWidgets.QLineEdit(DialogoCreacionBaseDeDatos)
        self.txt_nombre_base_datos.setGeometry(QtCore.QRect(180, 40, 181, 20))
        self.txt_nombre_base_datos.setObjectName("txt_nombre_base_datos")
        self.btn_crear_base_datos = QtWidgets.QPushButton(DialogoCreacionBaseDeDatos)
        self.btn_crear_base_datos.setGeometry(QtCore.QRect(20, 80, 341, 23))
        self.btn_crear_base_datos.setObjectName("btn_crear_base_datos")
        self.lbl_resultado = QtWidgets.QLabel(DialogoCreacionBaseDeDatos)
        self.lbl_resultado.setGeometry(QtCore.QRect(26, 130, 331, 20))
        self.lbl_resultado.setText("")
        self.lbl_resultado.setObjectName("lbl_resultado")

        self.retranslateUi(DialogoCreacionBaseDeDatos)
        QtCore.QMetaObject.connectSlotsByName(DialogoCreacionBaseDeDatos)

    def retranslateUi(self, DialogoCreacionBaseDeDatos):
        _translate = QtCore.QCoreApplication.translate
        DialogoCreacionBaseDeDatos.setWindowTitle(_translate("DialogoCreacionBaseDeDatos", "Creacion de bases de datos"))
        self.lbl_nombre_base_de_datos.setText(_translate("DialogoCreacionBaseDeDatos", "Nombre de la Base de Datos:"))
        self.btn_crear_base_datos.setText(_translate("DialogoCreacionBaseDeDatos", "Crear base de datos"))