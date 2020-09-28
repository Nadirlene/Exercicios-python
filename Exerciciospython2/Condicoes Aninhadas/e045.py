from random import choice
from time import sleep
print('\033[1;35mVAMOS JOGAR JOKENPÔ!!\033[m')
print('Suas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA ')
lista = [ 'PEDRA', 'PAPEL', 'TESOURA']
escolha = int(input('Qual é a sua jogada? '))
if escolha == 0:
    opcaoJogador = 'PEDRA'
elif escolha == 1:
    opcaoJogador = 'PAPEL'
else:
    opcaoJogador = 'TESOURA'
print('Jo')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
opcãoMáquina = choice(lista)
print('-=' * 11)
print('computador jogou {} \nJogador jogou {}'.format(opcãoMáquina, opcaoJogador))
print('-=' * 11)
if opcaoJogador == opcãoMáquina:
    print('EMPATE')
elif opcaoJogador == 'PEDRA' and opcãoMáquina == 'PAPEL':
    print('MÁQUINA VENCE')
elif opcaoJogador == 'PEDRA' and opcãoMáquina == 'TESOURA':
    print('JOGADOR VENCE')
elif opcaoJogador == 'PAPEL' and opcãoMáquina == 'PEDRA':
    print('JOGADOR VENCE')
elif opcaoJogador == 'PAPEL' and opcãoMáquina == 'TESOURA':
    print('MÁQUINA VENCE')
elif opcaoJogador == 'TESOURA' and opcãoMáquina == 'PAPEL':
    print('JOGADOR VENCE')
elif opcaoJogador == 'TESOURA' and opcãoMáquina == 'PEDRA':
    print('MÁQUINA VENCE')

