from random import randint
print('-*'*20)
print('Vou pensar em um número entre 0 e 10, tente advinhar!')
print('-*'*20)
tentativas = 1
numeroAleatório = randint(0, 10)
print(numeroAleatório)
numeroJogador = int(input('Qual é o seu palpite? '))
while numeroAleatório != numeroJogador:
    if numeroJogador > numeroAleatório:
        numeroJogador = int(input('''Menos... Tente mais uma vez. 
        Qual é o seu palpite? '''))
    elif numeroJogador < numeroAleatório:
        numeroJogador = int(input('''Mais... Tente mais uma vez. 
        Qual é o seu palpite? '''))
    tentativas += 1
print('Acertou com {} tentativas. Parabéns'.format(tentativas))



