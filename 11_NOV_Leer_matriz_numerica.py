# PRG 102
# Clase del viernes 11 de noviembre
# Matrices numéricas

# Leer el número de filas, el número de columnas
# y los elementos de una matriz desde teclado
mat = []
n = int(input('Nro. de filas ... '))
m = int(input('Nro. de columnas ... '))

for j in range(n):
    fila = []
    for k in range(m):
        dato = int(input('mat[' + str(j) + '][' + str(k) + '] = '))
        fila.append(dato)
    mat.append(fila)
    print()

print(mat)

# Mostrar la matriz diagonal

# Suma de la diagonal principal