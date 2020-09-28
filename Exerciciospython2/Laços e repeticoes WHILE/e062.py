print('Gerador de PA')
print('-='*7)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroTermo
contador = 1
total = 0
resposta = 10
quantidadeDeTermos = 0
while resposta !=0:
    total += resposta
    while contador <= total:
        print(f'{termo} ->', end=' ')
        contador += 1
        termo += razao
        quantidadeDeTermos += 1
    print('PAUSA')
    resposta = int(input('Quantos termos quer mostrar a mais? '))
print('FIM')
print(f'A quantidade de termos mostrado foi {quantidadeDeTermos}')

