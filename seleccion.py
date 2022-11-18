# Ordenación por el método de SELECCION
# Clase: Vier. 18 de nov.

vec = [8, 5, 9, 6, 2]

n = len(vec)

for i in range(n-1):
    for k in range(i+1, n):
        if vec[i] >= vec[k]:
            aux = vec[i]
            vec[i] = vec[k]
            vec[k] = aux

print(vec)