# enumeracion exhaustiva

objetivo = int(input('Ingrese numero: '))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'El {objetivo} no tiene raiz cuadrada')
