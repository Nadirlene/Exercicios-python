lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
listaPar = list()
listaImpar = list()
for numeros in lista:
    if numeros % 2 == 0:
        listaPar.append(numeros)
    else:
        listaImpar.append(numeros)
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')

