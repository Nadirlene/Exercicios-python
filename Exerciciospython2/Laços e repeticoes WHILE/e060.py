'''from math import factorial
numero = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(numero)
print('O fatorial de {} é {}.'.format(numero, f))'''


numero = int(input('Digite um número para \ncalcular seu fatorial: '))
fatorial = 1
print('Calculando {}!'.format(numero), end=' ' )
while numero != 0:
    print('{}'.format(numero), end='')
    print(' x ' if numero > 1 else ' = ', end='')
    fatorial *= numero
    numero -= 1
print('{:,}'.format(fatorial))