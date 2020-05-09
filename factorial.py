def factorial(n):
    """
    Calcula el factorial de n
    n int > 0
    :return: n!
    """
    print(n)
    if n == 1:
        return 1

    return n * factorial(n - 1)


numero = int(input('Ingrese numero entero: '))
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')
