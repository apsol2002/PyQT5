# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoPizza.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class DialogPizza(object):
    def setupUi(self, DialogPizza):
        DialogPizza.setObjectName("DialogPizza")
        DialogPizza.resize(400, 253)
        self.lbl_precio_pizza = QtWidgets.QLabel(DialogPizza)
        self.lbl_precio_pizza.setGeometry(QtCore.QRect(40, 30, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio_pizza.setFont(font)
        self.lbl_precio_pizza.setObjectName("lbl_precio_pizza")
        self.chk_queso = QtWidgets.QCheckBox(DialogPizza)
        self.chk_queso.setGeometry(QtCore.QRect(40, 90, 121, 20))
        self.chk_queso.setObjectName("chk_queso")
        self.chk_aceitunas = QtWidgets.QCheckBox(DialogPizza)
        self.chk_aceitunas.setGeometry(QtCore.QRect(40, 120, 111, 20))
        self.chk_aceitunas.setObjectName("chk_aceitunas")
        self.chk_salsas = QtWidgets.QCheckBox(DialogPizza)
        self.chk_salsas.setGeometry(QtCore.QRect(40, 150, 131, 20))
        self.chk_salsas.setObjectName("chk_salsas")
        self.lbl_seleccion_salsas = QtWidgets.QLabel(DialogPizza)
        self.lbl_seleccion_salsas.setGeometry(QtCore.QRect(40, 60, 181, 16))
        self.lbl_seleccion_salsas.setObjectName("lbl_seleccion_salsas")
        self.label_3 = QtWidgets.QLabel(DialogPizza)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 221, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(DialogPizza)
        QtCore.QMetaObject.connectSlotsByName(DialogPizza)

    def retranslateUi(self, DialogPizza):
        _translate = QtCore.QCoreApplication.translate
        DialogPizza.setWindowTitle(_translate("DialogPizza", "Pizza Kiosa"))
        self.lbl_precio_pizza.setText(_translate("DialogPizza", "Precio pizsa de $150"))
        self.chk_queso.setText(_translate("DialogPizza", "Queso $45"))
        self.chk_aceitunas.setText(_translate("DialogPizza", "Aceitunas $30"))
        self.chk_salsas.setText(_translate("DialogPizza", "Salsas $55"))
        self.lbl_seleccion_salsas.setText(_translate("DialogPizza", "Selecciona los gustos extras:"))
