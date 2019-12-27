# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaSistema.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.relogioFundo = QtWidgets.QFrame(self.centralwidget)
        self.relogioFundo.setGeometry(QtCore.QRect(20, 20, 171, 71))
        self.relogioFundo.setStyleSheet("background-color: rgb(145, 131, 198);\n"
"border-radius: 10px;")
        self.relogioFundo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.relogioFundo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.relogioFundo.setObjectName("relogioFundo")
        self.relogio = QtWidgets.QLCDNumber(self.relogioFundo)
        self.relogio.setGeometry(QtCore.QRect(10, 10, 151, 51))
        self.relogio.setObjectName("relogio")
        self.frameConteudos = QtWidgets.QFrame(self.centralwidget)
        self.frameConteudos.setGeometry(QtCore.QRect(20, 100, 861, 431))
        self.frameConteudos.setStyleSheet("background-color: rgb(225, 219, 255);")
        self.frameConteudos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameConteudos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameConteudos.setObjectName("frameConteudos")
        self.frameBotoesSuperiores = QtWidgets.QFrame(self.centralwidget)
        self.frameBotoesSuperiores.setGeometry(QtCore.QRect(210, 10, 671, 81))
        self.frameBotoesSuperiores.setStyleSheet("background-color: rgb(225, 219, 255);")
        self.frameBotoesSuperiores.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBotoesSuperiores.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBotoesSuperiores.setObjectName("frameBotoesSuperiores")
        self.btEntradasSaidas = QtWidgets.QPushButton(self.frameBotoesSuperiores)
        self.btEntradasSaidas.setGeometry(QtCore.QRect(20, 10, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btEntradasSaidas.setFont(font)
        self.btEntradasSaidas.setStyleSheet("color: rgb(0, 170, 0);\n"
"border: 1px solid green;\n"
"border-radius: 10px;\n"
"hover:{\n"
"  border: 1px solid red;\n"
"}")
        self.btEntradasSaidas.setObjectName("btEntradasSaidas")
        self.btControleDiario = QtWidgets.QPushButton(self.frameBotoesSuperiores)
        self.btControleDiario.setGeometry(QtCore.QRect(240, 10, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btControleDiario.setFont(font)
        self.btControleDiario.setStyleSheet("color: rgb(0, 170, 0);\n"
"border: 1px solid green;\n"
"border-radius: 10px;")
        self.btControleDiario.setObjectName("btControleDiario")
        self.btEstatisticas = QtWidgets.QPushButton(self.frameBotoesSuperiores)
        self.btEstatisticas.setGeometry(QtCore.QRect(470, 10, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btEstatisticas.setFont(font)
        self.btEstatisticas.setStyleSheet("color: rgb(0, 170, 0);\n"
"border: 1px solid green;\n"
"border-radius: 10px;")
        self.btEstatisticas.setObjectName("btEstatisticas")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btEntradasSaidas.setText(_translate("MainWindow", "Entradas / Saidas"))
        self.btControleDiario.setText(_translate("MainWindow", "Controle Diario"))
        self.btEstatisticas.setText(_translate("MainWindow", "Estatisticas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
