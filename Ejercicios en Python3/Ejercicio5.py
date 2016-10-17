#Ejercicio5
try:
	salario = float(input("Intruduce el sueldo en bruto: "))
	porcen = float(salario*0.2)
	print ("El salario neto es de: ", salario-porcen)
except:
	print("ERROR: El dato introducido no era un numero")

