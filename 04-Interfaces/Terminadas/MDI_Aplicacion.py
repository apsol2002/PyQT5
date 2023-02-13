import sys
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow
from MDI import Ui_MainWindow


class MDI_Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mni_tabs.triggered.connect(self.vista_tabs)
        self.ui.mni_cascadas.triggered.connect(self.vista_cascadas)
        self.ui.mni_cuadricula.triggered.connect(self.vista_cuadricula)
        self.ui.mni_subventana.triggered.connect(self.vista_subventana)

    #   Sino  no se mostraban por defecto ...
        self.ui.mdiArea.addSubWindow(self.ui.win_primera_subventana)
        self.ui.mdiArea.addSubWindow(self.ui.win_segunda_subventana)

        #self.show()

    def vista_tabs(self):
        self.ui.mdiArea.setViewMode(1)

    def vista_cascadas(self):
        self.ui.mdiArea.cascadeSubWindows()

    def vista_cuadricula(self):
        self.ui.mdiArea.tileSubWindows()

    def vista_subventana(self):
        self.ui.mdiArea.setViewMode(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = MDI_Aplicacion()
    dialogo.show()

    sys.exit(app.exec_())
