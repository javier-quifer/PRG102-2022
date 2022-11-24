# Búsqueda Binaria
# Clase: 23 de Nov.

vec = [5, 10, 2, 7, 9]

# 1er Paso: Ordenar
vec.sort()

# 2do Paso: Conocer al elemento a buscar
buscado = 9

# 3er Paso: Calcular mid (posición central)
n = len(vec)
infe = 0
supe = n - 1


# 4to Paso
while infe<=supe:
    mid = (infe + supe) // 2
    if vec[mid] == buscado:
        print(buscado, ' fue encontrado')
        exit(0)
    elif buscado > vec[mid]:
        infe = mid + 1
    elif buscado < vec[mid]:
        supe = mid - 1

print('No se encontró')