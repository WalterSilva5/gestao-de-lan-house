from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_MainWindow
from datetime import datetime


class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        
        #transições entre telas
        self.tela.buttonEntradasESaidas.clicked.connect(self.mostrarframeEntradasESaidas)
        self.tela.buttonControle.clicked.connect(self.mostrarFrameControle)
        self.tela.buttonEstatisticas.clicked.connect(self.mostrarFrameEstatisticas)
        self.tela.buttonVendas.clicked.connect(self.mostrarFrameVendas)
        #fim transições entre telas

        #relogio
        #while True:
        #    now = datetime.now()
        #    self.tela.relogio.setText(now.strftime("%H:%M:%S"))


        #adicionar valor a tabela venda
        self.tela.buttonConfirmarEntradaVenda.clicked.connect(self.adicionarValorATabelaVenda)

        #fim adicionar valor a tabela venda
        rowPosition = self.tela.tabelaVendaItens.rowCount()
        self.tela.tabelaVendaItens.insertRow(rowPosition)

        self.tela.tabelaVendaItens.setItem(rowPosition , 0, QTableWidgetItem("text1"))
        self.tela.tabelaVendaItens.setItem(rowPosition , 1, QTableWidgetItem("text2"))
        self.tela.tabelaVendaItens.setItem(rowPosition , 2, QTableWidgetItem("text3"))
    #transições entre telas
    def mostrarframeEntradasESaidas(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameEntradasESaidas.show()
        
    def mostrarFrameControle(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameControle.show()

    def mostrarFrameEstatisticas(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameEstatisticas.show()

    def mostrarFrameVendas(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameVendas.show()

    def esconderTodosOsFramesDeUso(self):
        self.tela.frameControle.hide()
        self.tela.frameEntradasESaidas.hide()
        self.tela.frameEstatisticas.hide()
        self.tela.frameVendas.hide()
        self.tela.frameInicial.hide()

    #fim transições entre telas

    #relogio
    #fim relogio
    
    #adicionar valor a tabela venda
    def adicionarValorATabelaVenda(self):
        valor = self.tela.entradaValorVenda.toPlainText()
        print(valor)
    