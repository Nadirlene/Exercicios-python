cadastro = {}
gols = []
cadastro['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
cadastro['gols'] = gols[:]
cadastro['total'] = sum(gols)
print('-='*30)
print(cadastro)
print('-='*30)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {cadastro["nome"]} jogou {cadastro["total"]} partidas.')
for p, v in enumerate(gols):
    print(f'  => Na partida {p}, fez {v} gols.')
print(f'Foi um total de {cadastro["total"]} gols.')

'''for p, v in enumerate(cadastro['gols']):
    print(f'  => Na partida {p}, fez {v} gols.')
print(f'Foi um total de {cadastro["total"]} gols.')'''