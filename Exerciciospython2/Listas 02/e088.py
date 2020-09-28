from random import randint
from time import sleep
lista = []
jogos = []
print('-'*40)
titulo = 'JOGO NA MEGA SENA'
print(f'{titulo:^40}')
print('-'*40)
resposta = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= resposta:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-='*3, f'SORTEANDO {resposta} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, ' < BOA SORTE > ', '-='*5)
