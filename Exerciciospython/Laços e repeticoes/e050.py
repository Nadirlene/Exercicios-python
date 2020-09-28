soma = 0
quantidadeNumerosPares = 0
for contador in range(1, 7):
    número = int(input('Digite o {} número: '.format(contador)))
    if número % 2 == 0:
        soma+= número
        quantidadeNumerosPares += 1
print('Você informou {} números pares e a soma deles foi {}'.format(quantidadeNumerosPares, soma))


