# uso de diccionarios

my_dict = {
    'JuanS': 1,
    'Camila': 5,
    'Paula': 32,
    'Mario': 33
}

print(my_dict)
print(my_dict['Paula'])
print(my_dict.get('Pepe', 0))  # con este no se genera error si no existe, y devuelve un valor por defecto

my_dict['Paula'] = 33  # modifica el valor en ese key
my_dict['Nuevo'] = 100  # agrega un nuevo key y valor
print(my_dict)

del my_dict['Nuevo']  # borra el elemento del diccionario
print(my_dict)

for llave in my_dict.keys():
    print(llave)


for valor in my_dict.values():
    print(valor)


for llave, valor in my_dict.items():
    print(f'{llave} {valor}')


print('JuanS' in my_dict)
print('Pedro' in my_dict)

