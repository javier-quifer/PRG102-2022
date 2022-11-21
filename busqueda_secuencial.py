# Métodos de búsqueda
# Búsqueda secuencial. Clase 21 de Nov.
from carla import leer_vector

vec = leer_vector()

buscado = input('Introd. el nombre a buscar')
esta = False

for dato in vec:
    if buscado == dato:
        print(buscado , ' se encuentra en la lista')
        esta = True

if not esta:
    print('No se encuentra en la lista')

