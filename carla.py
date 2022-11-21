def leer_vector():
    n = int(input('Cuantos elementos tiene el vector ? ... '))

    vec = []
    for k in range(n):
        dato = input('Introd. un elemento ... ')
        vec.append(dato)

    return vec