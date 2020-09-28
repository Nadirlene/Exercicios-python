from random import randint
print('=-'*12)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*12)
vitoria = 0
while True:
    valorMaquina = randint(0, 10)
    #print(valorMaquina)
    valorJogador = int(input('Digite um valor: '))
    somaValores = valorJogador + valorMaquina
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {valorJogador} e o computador {valorMaquina}. Total de {somaValores}', end=' ')
    print('DEU PAR' if somaValores % 2 == 0 else 'DEU IMPAR')
    if escolha == 'P':
        if somaValores % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    if escolha == 'I':
        if somaValores % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você venceu {vitoria} vezes.')