print("13ºFactorial de un numero N")
def Factorial():
	Numero= int(input("Escriba un numero "))
	Factorial = 1
	for n in range (Numero):
		Factorial *= Numero
		Numero -= 1
	print("Resultado:",Factorial)
Factorial()
