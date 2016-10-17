#Ejercicio6
try:
	numa = int(input("Introduce numero un entero, por favor: "))
	numb = int(input("Introduce otro numero un entero, por favor: "))
	print ("Numero 1: ", numa,"Numero 2: ", numb,"Antes")
	numc = numa
	numa = numb
	numb = numc
	print ("Numero 1: ", numa,"Numero 2: ", numb,"Despues")
except:
	print("ERROR: El dato introducido no era un numero entero")

