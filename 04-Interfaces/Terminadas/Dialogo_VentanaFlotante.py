# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialogo_VentanaFlotante.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaFlotante_MainWindow(object):
    def setupUi(self, VentanaFlotante_MainWindow):
        VentanaFlotante_MainWindow.setObjectName("VentanaFlotante_MainWindow")
        VentanaFlotante_MainWindow.resize(581, 582)
        self.centralwidget = QtWidgets.QWidget(VentanaFlotante_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dockWidget = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget.setGeometry(QtCore.QRect(450, 230, 295, 241))
        self.dockWidget.setFloating(True)
        self.dockWidget.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.dockWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 251, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_usuario = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_usuario.setObjectName("txt_usuario")
        self.gridLayout.addWidget(self.txt_usuario, 0, 1, 1, 1)
        self.txt_contrasea = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_contrasea.setObjectName("txt_contrasea")
        self.gridLayout.addWidget(self.txt_contrasea, 1, 1, 1, 1)
        self.lbl_contrasea = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_contrasea.setObjectName("lbl_contrasea")
        self.gridLayout.addWidget(self.lbl_contrasea, 1, 0, 1, 1)
        self.lbl_usuario = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_usuario.setObjectName("lbl_usuario")
        self.gridLayout.addWidget(self.lbl_usuario, 0, 0, 1, 1)
        self.btn_ingresar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.gridLayout.addWidget(self.btn_ingresar, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(30, 20, 231, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.dockWidget.setWidget(self.dockWidgetContents)
        VentanaFlotante_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaFlotante_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        VentanaFlotante_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaFlotante_MainWindow)
        self.statusbar.setObjectName("statusbar")
        VentanaFlotante_MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(VentanaFlotante_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(VentanaFlotante_MainWindow)

    def retranslateUi(self, VentanaFlotante_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        VentanaFlotante_MainWindow.setWindowTitle(_translate("VentanaFlotante_MainWindow", "Programa principal"))
        self.dockWidget.setWindowTitle(_translate("VentanaFlotante_MainWindow", "Iniciar sesión"))
        self.lbl_contrasea.setText(_translate("VentanaFlotante_MainWindow", "Contraseña"))
        self.lbl_usuario.setText(_translate("VentanaFlotante_MainWindow", "Usuario"))
        self.btn_ingresar.setText(_translate("VentanaFlotante_MainWindow", "Ingresar"))
        self.label.setText(_translate("VentanaFlotante_MainWindow", "Iniciar sesión"))
        self.menuArchivo.setTitle(_translate("VentanaFlotante_MainWindow", "Archivo"))
