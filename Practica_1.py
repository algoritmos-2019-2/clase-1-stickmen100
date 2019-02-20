print("1º Los dos tipos de valores del tipo de datos booleanos son verdadero y falso, y se escriben True y False.")
print("2º Los 3 operadores booleanos son Or,And y Not.")
print("4º Los seis operadores de comparacion serian <,>,==,<=,>= y !=.")
print("5º La diferencia es que con el comparador solo comparas dos valores y con el de asignacion asignas un valor a una variable,la cual podria ir cambiando a como asignemos las condiciones iniciales.")
print("6º Una condicion es toda sentencia con la que se pueda dar la verdad o falsedad de alguna operacion que estemos realizando, en si se utiliza para comparar datos de las operaciones.")
print("7º Si tu programa se encuentra en un bucle infinito primero tenemos que saber el PID del programa con ps -ef nos arrojara un numero del programa deseado a aniquilar y despues tendremos que poner kill -9 ### (y el numero del programa).")
print("8º Mientras que cuando rompemos se utiliza para salir de un bucle cuando se da cierta condicion, en cambio el continuar el bucle no termina pero tampoco se ejecuta los siguientes pasos arrojandote al siguiente paso a traves del bucle.")
print("9º En funcionamiento los tres tipos de rango son iguales ya que los 3 por default te arrojan del 0 al 9, solamente que cambia la forma de escribir los rangos ya que de la primera forma va del 0 al 9 de 1 en uno por default del programa, pero en el segundo tu le estas ordenando que justamente vaya de 0 al 9, ya que de la primera forma en si no estariamos definiendo un origen, y de la tercera forma estamos defiendo tanto un origen como el salto que va a dar entre cada numero.")

print("Serie fibonacci")
def fib(m):
	x, y = 0,1
	while x < m:
		print(x, end=' ')
		x, y = y, x+y
	print()
fib(1000) 
