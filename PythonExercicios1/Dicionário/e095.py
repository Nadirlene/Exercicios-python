cadastro = {}
gols = []
time = []

while True:
    cadastro['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {c}? ')))
    cadastro['gols'] = gols[:]
    cadastro['total'] = sum(gols)
    time.append(cadastro.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*40)
print('cod', end=' ')
for k in cadastro.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar) '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i} fez {g} gols')