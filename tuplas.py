my_tupla = (1, 'dos', True)
print(my_tupla)

print(my_tupla[1])

no_es_tupla = (1) # esta forma de asignacion no crea una tupla, crea un entero
print(type(no_es_tupla))

es_tupla = (1,) # al agregar la coma, si genera una tupla
print(type(es_tupla))

"""
Esto genera error pues una tupla es inmutable, solo puede ser reasignada

es_tupla[0] = 2
print(es_tupla)
"""

otra_tupla = (2, 3, 4)
es_tupla += otra_tupla # no modificó es_tupla, sino que re-asigno por lo que asi es que se puede modificar una tupla
print(es_tupla)

# desempaquetado de tupoas
x, y, z = otra_tupla
print(f'x={x} - y={y} - z={z}')


def coordenadas():
    return (4, 5)


coordena = coordenadas()
print(coordena)

x, y = coordenadas()
print(f'x={x} - y={y}')

