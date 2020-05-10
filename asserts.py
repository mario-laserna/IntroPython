def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras


# print(primera_letra(['pepe', 'mario']))
# print(primera_letra(['pepe', 'mario', 3]))

try:
    print(primera_letra(['pepe', 'mario', '']))
except Exception as e:
    print(f'ERROR {e}')

print(5/'platzi')

