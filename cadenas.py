# ejemplo de print
print('aa')
print('123' * 3)
print('Hip ' * 3 + ' ' + 'Hurra')
print(f'{"Hip " * 3} hurra')

#ejemplo de funciones con cadena
my_str = 'Platzi'
print(len(my_str))
print(my_str[0])
print(my_str[1])
print(my_str[2:]) #el 2 es inclusivo
print(my_str[:3]) #el indice no es inclusivo
print(my_str[:-2]) 
print(my_str[::2]) #toda la cadena saltando de 2 en 2

#ejemplo de inputs
nombre = input('Cual es tu nombre: ')
print('Tu nombre es', nombre)
print(f'Tu nombre es {nombre}')

numero = input('escribe un numero: ')
print('numero', numero)
print(type(numero))

numero2 = int(input('escribe un numero: '))
print('numero', numero2)
print(type(numero2))