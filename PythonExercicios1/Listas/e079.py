lista = list()
while True:
    numero = (int(input('Digite um valor: ')))
    if numero in lista:
        print('Valor duplicado, não irei adicionar a lista!')
    else:
        lista.append(numero)
        print('Valor adicionado com sucesso...')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
#print(f'Os valores adicionados foram {sorted(lista)}')
lista.sort()
print(f'Os valores adicionados foram {lista}')

