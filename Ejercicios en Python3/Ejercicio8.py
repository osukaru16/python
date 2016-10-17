#Ejercicio8
try:
	numa = int(input("Introduce numero un entero: "))
	numb = int(input("Introduce otro numero un entero: "))
	if numa > numb:
		print("El primer numero ", numa," es mayor al segundo", numb)
	elif numa < numb:
		print("El primer numero ", numa," es menor al segundo", numb)
	else:
		print("Los dos son iguales ", numa)
except:
	print("ERROR: El dato introducido no era un numero entero")

