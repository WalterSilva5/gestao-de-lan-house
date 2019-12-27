from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_MainWindow

class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)

        self.tela.btEntradasSaidas.clicked.connect(self.mostrarframeEntradasSaidas)

    def mostrarframeEntradasSaidas(self):
        self.frameEntradasSaidas.show()
