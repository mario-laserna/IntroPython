"""
El resultado no va a ser 1.0 como se espera, sino 0.999999999 por la forma en que python
almacena los números reales
"""

x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')