lista = []
cadatsro = {}
lista = []
somaIdades = média = 0
while True:
    cadatsro['nome'] = str(input('Nome: '))
    while True:
        cadatsro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if cadatsro['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadatsro['idade'] = int(input('Idade: '))
    somaIdades += cadatsro['idade']
    lista.append(cadatsro.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if resposta == 'N':
        break
print('-='*30)
print(lista)
print(f'A)  Ao todo temos {len(lista)} cadastradas.')
média = somaIdades / len(lista)
print(f'B)  A média de idade é de {média:.2f} anos')
print(f'C)  As mulheres cadastradas foram ', end= '')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D)  Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print(' << ENCERROU >> ')

