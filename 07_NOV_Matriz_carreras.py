mat = []
# A) Leer los elementos de una matriz (cursos)
N = int(input('N ... '))

for k in range(N):
    print('Datos del ', k+1, ' ° curso: ')
    curso = input('Curso ... ')
    carrera = input('Carrera ... ')
    nro_est = int(input('Cantidad de estudiantes ... '))
    fila = [curso, carrera, nro_est]
    mat.append(fila)
    print()

# B) Mostrar los elementos de la matriz (Elemento por elemento)
for fila in mat:
    for dato in fila:
        print(dato, end=' ')
    print()

#################   T A R E A ####################################
# C) Mostrar el curso y la carrera con mayor número de estudiantes
