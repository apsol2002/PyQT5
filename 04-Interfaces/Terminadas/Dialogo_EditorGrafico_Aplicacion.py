import sys

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPaintEngine, QPainter, QMouseEvent
from Dialogo_EditorGrafico import Ui_EditorGrafico


class Dialogo_EditorGrafico_Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_EditorGrafico()
        self.ui.setupUi(self)

        self.posicion_1 = [0, 0]
        self.posicion_2 = [0, 0]
        self.tipo_dibujo = ''

        self.ui.mni_dibujar_circulo.triggered.connect(self.dibujar_circulo)
        self.ui.mni_dibujar_rectangulo.triggered.connect(self.dibujar_rectangulo)
        self.ui.mni_dibujar_linea.triggered.connect(self.dibujar_linea)

        self.ui.mni_cortar.triggered.connect(self.cortar)

        self.show()

    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)

        if self.tipo_dibujo == 'circulo':
            ancho = self.posicion_1[0]- self.posicion_2[0]
            alto = self.posicion_1[1]- self.posicion_2[1]

            rectangulo = QRect(self.posicion_1[0],self.posicion_1[1], ancho,alto)
            angulo_inicio = 0
            longitud_arco = 360 * 16
            qp.drawArc(rectangulo,angulo_inicio,longitud_arco)

        if self.tipo_dibujo == 'rectangulo':
            ancho = self.posicion_2[0]- self.posicion_1[0]
            alto = self.posicion_2[1]- self.posicion_1[1]
            qp.drawRect(self.posicion_1[0],self.posicion_1[1],ancho,alto)

        if self.tipo_dibujo == 'linea':
            qp.drawLine(self.posicion_1[0], self.posicion_1[1], self.posicion_2[0], self.posicion_2[0])

        qp.end()

    def mousePressEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.LeftButton:
            self.posicion_1[0], self.posicion_1[1], = event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event : QMouseEvent):
        self.posicion_2[0], self.posicion_2[1], = event.pos().x(), event.pos().y()
        self.update()

    def dibujar_circulo(self):
        self.ui.lbl_estado.setText('')
        self.tipo_dibujo = 'circulo'

    def dibujar_rectangulo(self):
        self.ui.lbl_estado.setText('')
        self.tipo_dibujo = 'rectangulo'

    def dibujar_linea(self):
        self.ui.lbl_estado.setText('')
        self.tipo_dibujo = 'linea'

    def configurar_pagina(self):
        self.ui.lbl_estado.setText('Se uso la opcion de configurar')

    def establecer_password(self):
        self.ui.lbl_estado.setText('Se uso la opcion de establecer password')

    def cortar(self):
        self.ui.lbl_estado.setText('Se uso la opcion de cortar')

    def copiar(self):
        self.ui.lbl_estado.setText('Se uso la opcion de copiar')

    def pegar(self):
        self.ui.lbl_estado.setText('Se uso la opcion de pegar')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_EditorGrafico_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
