# Métodos de búsqueda
# Búsqueda secuencial. Clase 21 de Nov.

vec = ['Ana', 'Pedro', 'Carla', 'Juan']

buscado = 'Ana'
esta = False

for dato in vec:
    if buscado == dato:
        print(buscado , ' se encuentra en la lista')
        esta = True

if not esta:
    print('No se encuentra en la lista')

