from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from model.entrada import Entrada
from model.saida import Saida
import threading, time
from datetime import datetime

class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        #transições entre telas
        self.tela.buttonEntradasESaidas.clicked.connect(self.mostrarframeEntradasESaidas)
        self.tela.buttonEstatisticas.clicked.connect(self.mostrarFrameEstatisticas)
        self.tela.buttonVendas.clicked.connect(self.mostrarFrameVendas)
        #fim transições entre telas

        #relogio
        contar = threading.Thread(target = self.contarSegundos)
        contar.daemon = True
        contar.start()
        #fim relogio

        #gerenciamento de venda
        self.totalVendaAtual = 0
        ##adicionar valor a tabela venda
        self.tela.buttonConfirmarEntradaVenda.clicked.connect(self.adicionarValorATabelaVenda)
        ##fim adicionar valor a tabela venda
        ##adicionar valor recebido venda
        self.tela.buttonAdicionarValorRecebidoVenda.clicked.connect(self.adicionarValorRecebidoVendaEGerarTroco)
        ##fim adicionar valor recebido venda
        ##finalizar venda e adicionar a base
        self.tela.buttonFinalizarVenda.clicked.connect(self.finalizarVenda)
        ##fim finalizar venda e adicionar a base
        #fim gerenciamento de venda
        #listagem Entradas e saidas
        #self.tela.buttonConfirmarEntrada.clicked.connect()
        #fim listagem entradas e saidas
        #adicionar entrada pela tela de listagem
        self.tela.buttonConfirmarEntrada.clicked.connect(self.adicionarEntradaPelaListagem)
        #fim adicionar entrada pela tela de listagem
        #adicionar saida pela tela de listagem
        self.tela.buttonConfirmarSaida.clicked.connect(self.adicionarSaidaPelaListagem)
        #fim adicionar saida pela tela de listagem
        
        #ajustar label de total geral
        self.calcularTotalGeralDeSaldo()
        #fim ajustar label total geral
    #transições entre telas
    def mostrarframeEntradasESaidas(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameEntradasESaidas.show()
        self.atualizarJanelas()

    def atualizarJanelas(self):
        self.listarEntradas()
        self.listarSaidas()
        self.calcularTotalGeralDeSaldo()

        
    def mostrarFrameEstatisticas(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameEstatisticas.show()

    def mostrarFrameVendas(self):
        self.esconderTodosOsFramesDeUso()
        self.tela.frameVendas.show()

    def esconderTodosOsFramesDeUso(self):
        self.tela.frameEntradasESaidas.hide()
        self.tela.frameEstatisticas.hide()
        self.tela.frameVendas.hide()
        self.tela.frameInicial.hide()

    #fim transições entre telas

    #relogio
    def contarSegundos(self):
        while True:
            now = datetime.now()
            self.tela.relogio.setText(now.strftime("%H:%M:%S"))
            time.sleep(1)
    #fim relogio
    
    #adicionar valor a tabela venda
    def adicionarValorATabelaVenda(self):
        valor = self.tela.entradaValorVenda.toPlainText()
        atual = self.tela.tabelaVendaItens.rowCount()
        self.tela.tabelaVendaItens.insertRow(atual)
        self.tela.tabelaVendaItens.setItem(atual , 0, QTableWidgetItem(valor))
        
        self.totalVendaAtual += float(valor)
        self.tela.labelTotalVenda.setText("Total: {}".format(self.totalVendaAtual))
    #fim adicionar valor a tabela venda

    #adicionar valor recebido venda e gerar troco
    def adicionarValorRecebidoVendaEGerarTroco(self):
        recebido = self.tela.entradaValorRecebidoVenda.toPlainText()
        troco = float(recebido) - float(self.totalVendaAtual)
        self.tela.labelTroco.setText("Troco: {}".format(troco))
    #fim adicionar valor recebido venda
    #finalizar venda
    def finalizarVenda(self):
        entrada = Entrada()
        if self.totalVendaAtual != 0:
            entrada.adicionarEntrada(self.totalVendaAtual, "venda")
            limpar = threading.Thread(target = self.limparTelaVenda)
            limpar.daemon = True
            limpar.start()
            self.atualizarJanelas()
         
    def limparTelaVenda(self):
        self.tela.entradaValorVenda.clear()
        self.tela.labelTroco.setText("Troco:")
        self.tela.tabelaVendaItens.setRowCount(0)
        self.tela.labelTotalVenda.setText("Total:")
        self.tela.entradaValorRecebidoVenda.clear()
        self.totalVendaAtual = 0
    #fim finalizar venda

    #listar entradas e saidas na tela de listagem
    def listarEntradas(self):
        self.tela.tabelaEntradas.setRowCount(0)
        entrada = Entrada()
        entradas = entrada.listarEntradas()
        for elemento in entradas:
            atual = self.tela.tabelaEntradas.rowCount()
            self.tela.tabelaEntradas.insertRow(atual)
            self.tela.tabelaEntradas.setItem(atual , 0, QTableWidgetItem(str(elemento[0])))     
            self.tela.tabelaEntradas.setItem(atual , 1, QTableWidgetItem(str(elemento[1])))     
            self.tela.tabelaEntradas.setItem(atual , 2, QTableWidgetItem(str(elemento[2])))     
            self.tela.tabelaEntradas.setItem(atual , 3, QTableWidgetItem(str(elemento[3])))     
    #fim listar entradas e saidas na tela de listagem
    #listar saidas na tela de listagem
    def listarSaidas(self):
        self.tela.tabelaSaidas.setRowCount(0)
        saida = Saida()
        saidas = saida.listarSaidas()
        for elemento in saidas:
            atual = self.tela.tabelaSaidas.rowCount()
            self.tela.tabelaSaidas.insertRow(atual)
            self.tela.tabelaSaidas.setItem(atual , 0, QTableWidgetItem(str(elemento[0])))     
            self.tela.tabelaSaidas.setItem(atual , 1, QTableWidgetItem(str(elemento[1])))     
            self.tela.tabelaSaidas.setItem(atual , 2, QTableWidgetItem(str(elemento[2])))        
    #fim listar saidas na tela de listagem
    #adicionar valor entrada pela janela de listagem
    def adicionarEntradaPelaListagem(self):
        try:
            valor = float(self.tela.entradaValorEntrada.toPlainText())
        except:
            print("ocorreu um erro")
        else:
            if(self.tela.radioButtonXbox.isChecked()):
                tipo = "xbox"
            else:
                tipo = "pc"
            if valor != 0:
                entrada = Entrada()
                entrada.adicionarEntrada(valor, tipo)
                self.tela.entradaValorEntrada.clear()
                self.atualizarJanelas()
    #fim adicionar valor entrada pela janela de listagem
    #adicionar valor saida pela tela de listagem
    def adicionarSaidaPelaListagem(self):
        try:
            valor = float(self.tela.entradaValorSaida.toPlainText())
        except:
            print("ocorreu um erro")
        else:
            if valor != 0:
                saida = Saida()
                saida.adicionarSaida(valor)
                self.tela.entradaValorSaida.clear()
                self.atualizarJanelas()
    #fim adicionar valor saida pela tela de listagem

    #total geral de saldo
    def calcularTotalGeralDeSaldo(self):
        totalEntradas = 0
        totalSaidas = 0
        entradas = Entrada().listarEntradas()
        for entrada in entradas:
            totalEntradas += float(entrada[0])
        saidas = Saida().listarSaidas()
        for saida in saidas:
            totalSaidas += float(saida[0])
        totalGeral = totalEntradas - totalSaidas
        self.tela.labelTotal.setText("Total: {0:.2f}".format(totalGeral))
    #fim total geral de saldo