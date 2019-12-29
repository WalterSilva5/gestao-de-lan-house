from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_MainWindow

class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        self.tela.btEntradasESaidas.clicked.connect(self.mostrarframeEntradasESaidas)

    def mostrarframeEntradasESaidas(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameEntradasSaidas.show()
        
    def esconderTodosOsFramesDeUso(self):
        self.tela.frameControle.hide()
        self.tela.frameEntradasESaidas.hide()
        self.tela.frameEstatisticas.hide()
        self.tela.frameVendas.hide()
        self.tela.frameInicial.hide()