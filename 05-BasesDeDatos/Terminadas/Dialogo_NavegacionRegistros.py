# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialogo_NavegacionRegistros.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogo_NavegacionRegistros(object):
    def setupUi(self, Dialogo_NavegacionRegistros):
        Dialogo_NavegacionRegistros.setObjectName("Dialogo_NavegacionRegistros")
        Dialogo_NavegacionRegistros.resize(388, 157)
        self.widget = QtWidgets.QWidget(Dialogo_NavegacionRegistros)
        self.widget.setGeometry(QtCore.QRect(30, 20, 322, 125))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_id = QtWidgets.QLabel(self.widget)
        self.lbl_id.setObjectName("lbl_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_id)
        self.txt_id = QtWidgets.QLineEdit(self.widget)
        self.txt_id.setReadOnly(True)
        self.txt_id.setObjectName("txt_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_id)
        self.lbl_nombre = QtWidgets.QLabel(self.widget)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre)
        self.txt_nombre = QtWidgets.QLineEdit(self.widget)
        self.txt_nombre.setReadOnly(True)
        self.txt_nombre.setObjectName("txt_nombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_nombre)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_primero = QtWidgets.QPushButton(self.widget)
        self.btn_primero.setObjectName("btn_primero")
        self.horizontalLayout.addWidget(self.btn_primero)
        self.btn_anterior = QtWidgets.QPushButton(self.widget)
        self.btn_anterior.setObjectName("btn_anterior")
        self.horizontalLayout.addWidget(self.btn_anterior)
        self.btn_siguiente = QtWidgets.QPushButton(self.widget)
        self.btn_siguiente.setObjectName("btn_siguiente")
        self.horizontalLayout.addWidget(self.btn_siguiente)
        self.btn_ultimo = QtWidgets.QPushButton(self.widget)
        self.btn_ultimo.setObjectName("btn_ultimo")
        self.horizontalLayout.addWidget(self.btn_ultimo)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem)

        self.retranslateUi(Dialogo_NavegacionRegistros)
        QtCore.QMetaObject.connectSlotsByName(Dialogo_NavegacionRegistros)

    def retranslateUi(self, Dialogo_NavegacionRegistros):
        _translate = QtCore.QCoreApplication.translate
        Dialogo_NavegacionRegistros.setWindowTitle(_translate("Dialogo_NavegacionRegistros", "Sqlite3 - Navegacion registro"))
        self.lbl_id.setText(_translate("Dialogo_NavegacionRegistros", "ID:"))
        self.lbl_nombre.setText(_translate("Dialogo_NavegacionRegistros", "Nombre:"))
        self.btn_primero.setText(_translate("Dialogo_NavegacionRegistros", "Primero"))
        self.btn_anterior.setText(_translate("Dialogo_NavegacionRegistros", "Anterior"))
        self.btn_siguiente.setText(_translate("Dialogo_NavegacionRegistros", "Siguiente"))
        self.btn_ultimo.setText(_translate("Dialogo_NavegacionRegistros", "Último"))