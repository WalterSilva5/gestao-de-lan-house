class Calculadora():
	def __init__(self):
		self.inicio()
	def inicio(self):
		self.mostrarTotal()
		print("Adicionar valor 'a'")
		print("Mostrar Total: m")
		print("Sair: s")

		op = input("Opção: ")
		if op == 'a':
			self.adicionarValor()
		elif op == 'm':
			self.mostrarTotal()
		elif op == 's':
			print("fim do programa")
			exit()
		else: 
			print("opção invalida")
			self.inicio()
	def mostrarTotal(self):
		total = 0
		arquivo = open("valores.txt", "r")
		valores = (arquivo.read()).split()
		for valor in valores:
			total += float(valor)
		arquivo.close()
		print("Total atual: {}".format(total))
	
cal = Calculadora()
