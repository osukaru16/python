#Ejercicio13
try:
	num = float(input("Introduce el valor bruto del articulo: "))
	if num <= 20:
		print("El valor del articulo es: ",num)
	elif num > 20 and num <= 100:
		print("El valor del articulo es: ",num-num*0.05)
	elif num > 100:
		print("El valor del articulo es: ",num-num*0.10)
except:
	print("ERROR: El dato introducido no era un numero entero")

