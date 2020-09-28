print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
primeiroTermo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiroTermo + (10 - 1) * razão
for contador in range(primeiroTermo, décimo + razão, razão):
    print(contador,'->', end=' ')
print('ACABOU')
