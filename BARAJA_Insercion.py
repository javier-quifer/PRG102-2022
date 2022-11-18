# Método de ordenación: Inserción o BARAJA
# Clase: Juev. 17 de NOV.

vec = [34, 25, 54, 15, 60, 45, 30, 20, 8]
#vec = []
n = len(vec)
print(vec)

for j in range(1, n):
    carta = vec[j]
    k = j -1

    while carta<=vec[k] and k>=0:
        vec[k+1] = vec[k]
        k = k - 1

    vec[k+1] = carta

print(vec)