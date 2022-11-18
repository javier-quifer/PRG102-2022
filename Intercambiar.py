# Intercambio de dos variables (método tradicional)

a = int(input('Introd. el 1er nro '))
b = int(input('Introd. el 2do nro '))

aux = a
a = b
b = aux

print(a, b)