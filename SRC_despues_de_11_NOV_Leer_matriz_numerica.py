# PRG 102
# Clase del viernes 11 de noviembre
# Matrices numéricas

# Leer el número de filas, el número de columnas
# y los elementos de una matriz desde teclado
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [3, 4, 1]]
# n = int(input('Nro. de filas ... '))
# m = int(input('Nro. de columnas ... '))
#
# for j in range(n):
#     fila = []
#     for k in range(m):
#         dato = int(input('mat[' + str(j) + '][' + str(k) + '] = '))
#         fila.append(dato)
#     mat.append(fila)
#     print()

#print(mat)
#B) Mostrar la matriz, elemento por elemento
n = len(mat)
for j in range(n):
    m = len(mat[j])
    for k in range(m):
        if j==0 and k==0:
            print('┌  ', end='') #218

        if j>0 and j<n-1 and k==0:
            print('|  ', end='')

        if j==n-1 and k==0:
            print('└  ', end='') #192

        print(mat[j][k], end='  ')

        if j==0 and k==m-1:
            print('┐', end='') #191

        if j>0 and j<n-1 and k==m-1:
            print('|', end='')

        if j==n-1 and k==m-1:
            print('┘') #217

    print()




# Mostrar la matriz diagonal

# Suma de la diagonal principal