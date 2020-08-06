def primaria(objetivo, epsilon):
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def aproximacion(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es la {respuesta}')



menu = """ Bienvenido a la calculadora de números cuadrados

1 - Búsqueda con aproximación
2 - Búsqueda primaria

Elige una opción: """

opcion = int(input(menu))


if opcion == 1:
    objetivo = int(input('Escoge un numero: '))
    epsilon = float(input('Escoge una aproximación: '))
    primaria(objetivo, epsilon)
elif opcion == 2:
    objetivo = int(input('Escoge un numero: '))
    aproximacion(objetivo)
else: 
    print('Ingresa una opción correcta')

