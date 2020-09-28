número = int(input('Digite um numero: '))
quantidadeDivisores = 0
for contador in range(1 , número+1):
    if número  % contador == 0:
        quantidadeDivisores += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(contador), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(número, quantidadeDivisores))
if quantidadeDivisores == 2:
    print('E por isso ele é PRIMO! ')
else:
    print('E por isso ele NÃO é PRIMO! ')
    