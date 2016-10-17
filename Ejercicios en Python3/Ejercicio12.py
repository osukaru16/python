#Ejercicio12
try:
	print("Tendras que poner dos numeros enteros y que sean pares")
	numa = int(input("Introduce el primer numero un entero: "))
	numb = int(input("Introduce el segundo numero un entero: "))
	if numa % 2 == 0 and numb % 2 == 0:
		if numa < 50:
			if numb >= 100 and numb <= 500:
				print("El resultado de la suma es: ",numa+numb)
			else:
				print("El segundo numero tiene que ser entre 100 a 500")
		else:
			print("El primer numero tiene que es menor de 50")
	else:
		print("Alguno de los numeros no es par")
except:
	print("ERROR: El dato introducido no era un numero entero")

