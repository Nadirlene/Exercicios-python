print('Gerador de PA')
print('-='*7)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroTermo
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end=' ')
    termo += razao
    contador += 1
print('FIM')
