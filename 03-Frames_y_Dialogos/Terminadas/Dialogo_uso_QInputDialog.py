import sys
from PyQt5.QtWidgets import QApplication,QDialog,QInputDialog,QPushButton,QLabel

class Dialogo_uso_inputDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Uso de QInputDialog')
        self.setGeometry(500,400,300,200)

        btn_capturar_datos = QPushButton('Capturar Datos', self)
        btn_capturar_datos.move(30,30)
        btn_capturar_datos.clicked.connect(self.capturar_datos)

        self.show()

    def capturar_datos(self):

        lbl_resultados = QLabel(self)
        lbl_resultados.move(30,60)

        valores= []

        # Captura de enteros
        entero, _ = QInputDialog.getInt(self, 'Captura ENTEROS', 'Ingresa un mumero', 2,1,100,1 )
        valores.append(entero)

        # Captura de reales
        real, _ = QInputDialog.getDouble(self, 'Captura REALES', 'Ingresa un mumero real', 3.1245,1,100,2 )
        valores.append(entero)

        # Captura una opcion
        colores = ['Rojo','Azul','Verde']
        color, _ = QInputDialog.getItem(self, 'Captura OPCIONES', 'Escoja una opcion', colores, 0, False )
        valores.append(color)

        # Captura de Texto
        texto = QInputDialog.getText(self,"Captura TEXTO",'Escribe tu nombre')
        valores.append(texto)

        datos = f'{valores[0]}, {valores[1]}, {valores[2]}, {valores[3]}'
        # ', '.join( [str(valor) for valor in valores] )
        lbl_resultados.setText(datos)
        lbl_resultados.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_uso_inputDialog()
    dialogo.show()

    sys.exit(app.exec_())




