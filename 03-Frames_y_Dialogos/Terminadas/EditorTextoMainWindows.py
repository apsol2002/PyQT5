# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorTextoMainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditorTextoMainWindows(object):
    def setupUi(self, EditorTextoMainWindows):
        EditorTextoMainWindows.setObjectName("EditorTextoMainWindows")
        EditorTextoMainWindows.resize(501, 538)
        self.centralwidget = QtWidgets.QWidget(EditorTextoMainWindows)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_texto = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_texto.setGeometry(QtCore.QRect(10, 10, 481, 481))
        self.txt_texto.setObjectName("txt_texto")
        EditorTextoMainWindows.setCentralWidget(self.centralwidget)
        self.mbr_principal = QtWidgets.QMenuBar(EditorTextoMainWindows)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 501, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        self.mnu_archivo = QtWidgets.QMenu(self.mbr_principal)
        self.mnu_archivo.setObjectName("mnu_archivo")
        EditorTextoMainWindows.setMenuBar(self.mbr_principal)
        self.statusbar = QtWidgets.QStatusBar(EditorTextoMainWindows)
        self.statusbar.setObjectName("statusbar")
        EditorTextoMainWindows.setStatusBar(self.statusbar)
        self.mni_abrir = QtWidgets.QAction(EditorTextoMainWindows)
        self.mni_abrir.setObjectName("mni_abrir")
        self.mni_guardar = QtWidgets.QAction(EditorTextoMainWindows)
        self.mni_guardar.setObjectName("mni_guardar")
        self.mni_salir = QtWidgets.QAction(EditorTextoMainWindows)
        self.mni_salir.setObjectName("mni_salir")
        self.mnu_archivo.addAction(self.mni_abrir)
        self.mnu_archivo.addAction(self.mni_guardar)
        self.mnu_archivo.addSeparator()
        self.mnu_archivo.addAction(self.mni_salir)
        self.mbr_principal.addAction(self.mnu_archivo.menuAction())

        self.retranslateUi(EditorTextoMainWindows)
        QtCore.QMetaObject.connectSlotsByName(EditorTextoMainWindows)

    def retranslateUi(self, EditorTextoMainWindows):
        _translate = QtCore.QCoreApplication.translate
        EditorTextoMainWindows.setWindowTitle(_translate("EditorTextoMainWindows", "Editor Texto"))
        self.mnu_archivo.setTitle(_translate("EditorTextoMainWindows", "Archivo"))
        self.mni_abrir.setText(_translate("EditorTextoMainWindows", "Abrir"))
        self.mni_abrir.setShortcut(_translate("EditorTextoMainWindows", "Ctrl+A"))
        self.mni_guardar.setText(_translate("EditorTextoMainWindows", "Guardar"))
        self.mni_guardar.setShortcut(_translate("EditorTextoMainWindows", "Ctrl+G"))
        self.mni_salir.setText(_translate("EditorTextoMainWindows", "Salir"))
        self.mni_salir.setShortcut(_translate("EditorTextoMainWindows", "Ctrl+S"))
