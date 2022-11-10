# PRG102: Clase del Mierc. 9 de Noviembre

# Generar las posiciones o índices

# n = int(input('Nro. de filas ... '))
# m = int(input('Nro. de columnas ... '))
#
# for j in range(n):
#     for k in range(m):
#         print(j, k, end='   ')
#     print()

#
mat = [[2, 6],
       [8, 1, 9]]

n = len(mat)
for j in range(n):
    m = len(mat[j])
    for k in range(m):
        print(mat[j][k], end='   ')
    print()

# Sumar los elementos de la matriz
suma = 0
n = len(mat)
for j in range(n):
    m = len(mat[j])
    for k in range(m):
        suma = suma + mat[j][k]

print('La suma es = ', suma)
