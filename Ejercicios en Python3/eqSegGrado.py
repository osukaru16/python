#Equaciones 
import math
a = 1
b = -7
c = 10


def resEquacionSegundoGrado(a,b,c):
	res1 = ((-b+math.sqrt(b**2-4*a*c))/2*a)
	res2 = ((-b-math.sqrt(b**2-4*a*c))/2*a)
	return res1, res2



x1, x2 = resEquacionSegundoGrado(a, b, c)

	

	
	
if x1 == 5 and x2 == 2:
	print("Pasa la prueba", x1, x2)
else:
	print("No pasa", x1 , x2)
	
	
	
	


