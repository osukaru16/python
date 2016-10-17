#Ejercicio10
try:
	numa = int(input("Introduce numero un entero: "))
	numb = int(input("Introduce otro numero un entero: "))
	if numa < 0 and numb < 0:
		print("No se puede realizar la suma porque los dos numeros son negativos")
	elif numa < 0:
		print("No se puede realizar la suma porque el primer numero es negativo")
	elif numb < 0:
		print("No se puede realizar la suma porque el segundo numero es negativo")
	else:
		print("La suma de los dos numeros es: ", numa+numb)
except:
	print("ERROR: El dato introducido no era un numero entero")

