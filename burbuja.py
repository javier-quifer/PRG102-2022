# Ordenación por el método de BURBUJA
# Clase: Mierc. 16 Nov.

vec = [6, 5, 3, 1, 8, 7, 2, 4]
print('Vector inicial:')
print(vec)

n = len(vec)

for j in range(n-1):
    for k in range(n-1):
        if vec[k] > vec[k+1]:
            aux = vec[k]
            vec[k] = vec[k+1]
            vec[k+1] = aux

print('vector ordenado:')
print(vec)