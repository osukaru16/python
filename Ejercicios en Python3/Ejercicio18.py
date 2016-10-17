#Ejercicio18

try:
	numMax = int(input("Introduce numero: "))
	for i in range(1, numMax+1):
		print ("2 X ",i,"=",i*2)
except:
	print("ERROR: El dato introducido no era un numero entero")