lista = []
while True:
    nome = str(input('Nome: '))
    Nota1 = float(input('Nota 1: '))
    Nota2 = float(input('Nota 2: '))
    media = (Nota1 + Nota2) / 2
    lista.append([nome, [Nota1, Nota2], media])
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(lista)
print('-='*40)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*35)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*35)
while True:
    print('-='*35)
    escolha = int(input('Mostrar notas de qual aluno? [999 interromper]: '))
    if escolha == 999:
        print('FINALIZANDO...')
        break
    elif escolha <= len(lista)-1:
        print(f'Notas de {lista[escolha][0]} são {lista[escolha][1]}')
print('<<< VOLTE SEMOPRE >>>')

