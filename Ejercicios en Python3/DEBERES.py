﻿# Ejercicio propuesto por Guillermo Cirer
# Lesson 2: Problem set (Optional 2)
# Superhero Nuisance
# Enunciado del ejercicio:
# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

def fix_machine(escombrera, producto):
	mensajeError = "Give me something that's not useless next time."
	posicion = 0
	productoConstruido = ""
	try:
		while escombrera.find(producto[posicion]) >= 0:
			productoConstruido = productoConstruido + producto[posicion]
			posicion += 1

	except(IndexError):		
		if productoConstruido == producto:
			return productoConstruido
		else:
			return mensajeError
	
	

# TEST CASES funcion fix_machine
print("Prueba: ", fix_machine('asdfghjklowern', 'leon'))
print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time.")
print("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity')
print("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity')
print("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt')
print("Test case 5: ", fix_machine('matrix reloaded', 'dedo mixta lordo') == 'dedo mixta lordo')