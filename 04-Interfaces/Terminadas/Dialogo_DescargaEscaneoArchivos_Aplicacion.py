import random
import sys
import threading
import time
from PyQt5.QtWidgets import QApplication, QDialog
from Dialogo_DescargasYEscaneoArchivos import *


class Dialogo_DescargaEscaneoArchivos_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_DescargaEscaneoArchivos()
        self.ui.setupUi(self)

        # self.ui.chk_chocolate.stateChanged.connect(self.calcular_precio)

class ProcesoSegundoPlano(threading.Thread):
    def __init__(self, dialogo, progress_bar:QtWidgets.QProgressBar):
        threading.Thread.__init__(self)

        self.dialogo = dialogo
        self.progress_bar = progress_bar
        self.contador = 0

    def run(self):
        bloqueo.acquire()
        while self.contador <= 100:
            time.sleep(1)

            self.progress_bar.setValue(self.contador)
            self.contador += random.randint(a=2, b=10)


        if self.contador >= 100:
            self.progress_bar.setValue(100)
            time.sleep(1)

        bloqueo.release()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogo = Dialogo_DescargaEscaneoArchivos_Aplicacion()
    dialogo.show()

    t_1 = ProcesoSegundoPlano(dialogo, dialogo.ui.pgr_descarga_archivo)
    t_2 = ProcesoSegundoPlano(dialogo, dialogo.ui.pgr_escaneo_amenazas)

    bloqueo = threading.Lock()

    t_1.start()
    t_2.start()

    #t_1.join()
    #t_2.join()

    sys.exit(app.exec_())
