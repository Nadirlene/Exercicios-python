def ficha(nome='<desconhecido>', gol=0,):
    print( f'O jogador {nome} fez {gol} gol(s) no campeonato.')


nomeJogador = str(input('Nome do jogador: '))
numGols = str(input('Número de gols: '))
if numGols.isnumeric():
    numGols = int(numGols)
else:
    numGols = 0
if nomeJogador.strip() == '':
    ficha(gol=numGols)
else:
    ficha(nomeJogador, numGols)
