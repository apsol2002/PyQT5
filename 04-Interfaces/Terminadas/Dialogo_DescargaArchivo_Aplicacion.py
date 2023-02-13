import sys
import threading
import time
from PyQt5.QtWidgets import QApplication, QDialog
from Dialogo_DescargaArchivos import *


class Dialogo_DescargaArchivo_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialogo_DescargaArchivo()
        self.ui.setupUi(self)

        #self.ui.pbr_descarga_archivo.setValue()

class ProcesoDescargaArchivos(threading.Thread):
    contador = 0

    def __init__(self, dialogo):
        threading.Thread.__init__(self)
        self.dialogo = dialogo

        self.contador = 0

    def run(self):
        while self.contador <= 100:
            time.sleep(1)
            self.dialogo.ui.pbr_descarga_archivo.setValue(self.contador)
            self.contador += 10


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_DescargaArchivo_Aplicacion()

    t = ProcesoDescargaArchivos(dialogo)
    t.start()

    dialogo.show()

    sys.exit(app.exec_())
