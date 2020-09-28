listaInicial = []
listaFinal = []
maior = menor = 0
while True:
    listaInicial.append(str(input('Nome: ')))
    listaInicial.append(int(input('Peso: ')))
    if len(listaFinal) == 0:
        maior = menor = listaInicial[1]
    else:
        if listaInicial[1] > maior:
            maior = listaInicial[1]
        elif listaInicial[1] < menor:
            menor = listaInicial[1]
    listaFinal.append(listaInicial[:])
    listaInicial.clear()
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(listaFinal)
print(f'Foram cadastradas {len(listaFinal)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end= '')
for p in listaFinal:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
        print()
print(f'O menor peso foi de {menor}. Peso de ', end='')
for p in listaFinal:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

