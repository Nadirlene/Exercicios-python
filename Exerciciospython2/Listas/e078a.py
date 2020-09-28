lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]
print('=-'*20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for posicao, valor in enumerate(lista):
    if valor == maior:
        print(f'{posicao}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for posicao, valor in enumerate(lista):
    if valor == menor:
        print(f'{posicao}...', end=' ')
print()
