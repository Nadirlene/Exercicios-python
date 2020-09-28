lista = list()
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    else:
        posição = 0
        while posição < len(lista):
            if numero <= lista[posição]:
                lista.insert(posição, numero)
                break
            posição += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
