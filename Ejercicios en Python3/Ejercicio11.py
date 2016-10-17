#Ejercicio11
try:
	print("Tendras que poner tres numeros enteros y que sumando dos de ellos el resultado sea el tercero")
	numa = int(input("Introduce el primer numero un entero: "))
	numb = int(input("Introduce el segundo numero un entero: "))
	numc = int(input("Introduce el tercer numero un entero: "))
	print("Los numeros introducidos son: ",numa, numb, numc)
	if numa + numb == numc:
		print("Se cumple N1+N2=N3")
	elif numa + numc == numb:
		print("Se cumple N1+N3=N2")
	elif numb + numc == numa:
		print("Se cumple N2+N3=N1")
	else:
		print("No se cumple las condiciones ")
except:
	print("ERROR: El dato introducido no era un numero entero")

