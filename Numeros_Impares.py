def xNumerosImpares(j, m):

	if( m > 0):
		print(str((j*2)-1))
		xNumerosImpares( j+1, m-1 )
m = int(input("Determinar cantidad de numeros que desee: "))
xNumerosImpares(1,m)
