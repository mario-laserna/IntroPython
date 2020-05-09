rango = range(1, 5)
for i in rango:
    print(i)

rango = range(0, 7, 2)
rango2 = range(0, 8, 2)

for i in rango:
    print(i)

for i in rango2:
    print(i)

print(rango == rango2)
print(rango is rango2) # compara igualdad entre objetos
print(id(rango))
print(id(rango2))

for i in range(1, 100, 2):
    print(i)
