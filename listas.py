# listas en python

my_list = [1, 2, 3]

print(my_list[0])
print(my_list[1:])

my_list.append(4)
print(my_list)

my_list[0] = 'a'
print(my_list)

sacado = my_list.pop()
print(sacado)
print(my_list)

# iteración
for element in my_list:
    print(element)


""" 
    No se debe realizar asignación directa para copiar una lista en otra variable,
    pues esto lo que hace es crear una referencia al mismo objeto
"""
a = [1, 2]
b = a
print(id(a))  # ambos tiene el mismo id
print(id(b))  # ambos tiene el mismo id
a.append(3)
print(b)  # b se ve afectado a pesar que el append fue en a

c = list(a)
d = a[::]

print(id(c))
print(id(d))

"""
    List comprehension
    Es posible asignar filtros a las listas para transformar la salida u obtener solo una parte de esta
"""
uno_a_cien = list(range(100)) # crea una lista del 0 al 99
print(uno_a_cien)

double = [i * 2 for i in uno_a_cien] # hace un ciclo y a cada elemento lo multiplica por dos
print(double)

pares = [i for i in uno_a_cien if i % 2 == 0]
print(pares)

