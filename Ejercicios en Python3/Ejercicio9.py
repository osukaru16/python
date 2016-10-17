#Ejercicio9
try:
	numa = int(input("Introduce numero un entero: "))
	numb = int(input("Introduce otro numero un entero: "))
	if numa < 0 or numb < 0:
		print("No se puede realizar la suma porque alguno de los numeros es negativo")
	else:
		print("La suma de los dos numeros es: ", numa+numb)
except:
	print("ERROR: El dato introducido no era un numero entero")

