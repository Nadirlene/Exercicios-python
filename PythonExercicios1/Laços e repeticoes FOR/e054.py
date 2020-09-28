import datetime
maiorIdade = 0
menorIdade = 0
anoAtual = datetime.date.today().year
for contador in range(1, 8):
    anoNascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(contador)))
    idadePessoa = anoAtual - anoNascimento
    print(idadePessoa)
    if idadePessoa >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} menores de idade'''.format(maiorIdade, menorIdade))
