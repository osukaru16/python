def maker(N):
	def action(X):		# Make and return action
		return X ** N 	# action retains N from enclosing scope
	return action
f = maker(88)
dato = int(input("Introduce numero: "))
print(f(dato))