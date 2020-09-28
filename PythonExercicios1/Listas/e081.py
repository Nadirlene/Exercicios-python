lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'VocÊ digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores digitados em ordem descrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')