"""import random
#print(random.uniform(0,999))
numero = float(input(random.randint(0,999)))
print(numero)
separado = numero.split()
print(separado)"""
"""numero = (int(input('Informe um número: ')))
n = str(numero)
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))"""

numero = int(input('Informe um número: '))
print('Analisando o número {}'.format(numero))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero //1000
# m = numero // 1000 % 10
print('Unidade: {} \nDezena: {} \nCenteza: {}  \nMilhar: {}'.format(u, d, c, m))
