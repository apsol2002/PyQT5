import sys
from PyQt5.QtWidgets import QAction, QApplication,QFileDialog, QMainWindow
from EditorTextoMainWindows import *


class EditorTextoMainWindows_Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_EditorTextoMainWindows()
        self.ui.setupUi(self)

        self.ui.mni_abrir.triggered.connect(self.abrir)
        self.ui.mni_guardar.triggered.connect(self.guardar)
        self.ui.mni_salir.triggered.connect(self.salir)

        self.show()

    def abrir(self):
        archivo = QFileDialog.getOpenFileName(self, 'Abrir Archivo', 'C:\\', '.txt')

        if archivo[0]:
            with open(archivo[0], 'rt') as f:
                datos = f.read()
                self.ui.txt_texto.setText(datos)

    def guardar(self):
        option = QFileDialog.Options()
        option != QFileDialog.DontUseNativeDialog

        archivo, _ = QFileDialog.getSaveFileName(self, 'Guardar Archivo', 'C:\\', 'Archivo de texto (.txt)', options=option)
        with open(archivo, 'wt') as f:
            f.write(self.ui.txt_texto.toPlainText())

    def salir(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = EditorTextoMainWindows_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
