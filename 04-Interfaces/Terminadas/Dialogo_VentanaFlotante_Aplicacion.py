import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from Dialogo_VentanaFlotante import Ui_VentanaFlotante_MainWindow


class VentanaFlotante_Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_VentanaFlotante_MainWindow()
        self.ui.setupUi(self)

        self.show()

        self.ui.btn_ingresar.clicked.connect(self.funcion)

    def funcion(self):
        self.ui.dockWidget.setWindowTitle("nuevo titulo")
        self.ui.dockWidget.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = VentanaFlotante_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
