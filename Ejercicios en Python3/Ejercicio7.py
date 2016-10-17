#Ejercicio7
try:
	num = int(input("Introduce numero un entero positivo o negativo: "))
	if num < 0:
		print("El numero ", num," es negativo")
	else:
		print("El numero ", num," es positivo")
except:
	print("ERROR: El dato introducido no era un numero entero")

