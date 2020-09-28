from random import randint
from time import sleep
númerosSorteados = []

def sorteio(lista):
    print(f'Sorteando {len(lista)} valores da lista:', end=' ')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteio(númerosSorteados)
somaPar(númerosSorteados)

