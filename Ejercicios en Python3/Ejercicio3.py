#Ejercicio3
try:
	radi = float(input("Introduce el radio de la circunferencia: "))
	pi = float(3.14159)
	print("La longitud de la cirunferencia es de: ", radi*2*pi)
	print("El area de la cirunferencia es de: ", pi*radi**2)
	
except:
	print("ERROR: El dato introducido no era un numero")