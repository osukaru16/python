#Ejercicio14 Ver 1
try:
	num = int(input("Introduce el valor bruto del articulo: "))
	#num = 2236
	resCien = int(num / 100)
	resCincuenta = int((num-resCien*100)/50)
	resVeinte = int(((num-resCien*100)-resCincuenta*50)/20)
	resDiez = int((((num-resCien*100)-resCincuenta*50)-resVeinte*20)/10)
	resCinco = int(((((num-resCien*100)-resCincuenta*50)-resVeinte*20)-resDiez*10)/5)
	resDos = int((((((num-resCien*100)-resCincuenta*50)-resVeinte*20)-resDiez*10)-resCinco*5)/2)
	resUno = int(((((((num-resCien*100)-resCincuenta*50)-resVeinte*20)-resDiez*10)-resCinco*5)-resDos*2)/1)
	print("De cien hay ",resCien," billetes")
	print("De cincuenta hay ",resCincuenta," billetes")
	print("De veinte hay ",resVeinte," billetes")
	print("De diez hay ",resDiez," billetes")
	print("De cinco hay ",resCinco," billetes")
	print("De dos hay ",resDos," monedas")
	print("De un hay ",resUno," monedas")
except:
	print("ERROR: El dato introducido no era un numero entero")
