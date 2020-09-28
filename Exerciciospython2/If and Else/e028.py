from random import randrange
from time import sleep
print('-=-'*37)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*37)
númeroAleatório = randrange(0, 5) #Faz o computador gerar o número
#print(númeroAleatório)
númeroDigitado = int(input('Em que número eu pensei? Digite: '))# Jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if númeroAleatório == númeroDigitado:
     print('PARABÉNS! Você conseguiu me vencer!')
else:
  print('GANHEI!! Eu pensei no número {} e não no {}!'.format(númeroAleatório, númeroDigitado))


