#Ejercicio4
try:
	base = float(input("Introduce la base en metros de la finca: "))
	altura = float(input("Introduce la altura en metros de la finca: "))

	print("La finca tiene: ", base*altura,"metros cuadrados")
	print("El perimetro de la finca tiene: ", base*2+altura*2,"metros")

	
except:
	print("ERROR: El dato introducido no era un numero entero")