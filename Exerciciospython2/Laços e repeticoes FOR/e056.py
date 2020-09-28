totalIdade = 0
mulherMenos20 = 0
idadeHomemVelho = 0
nomeHomemVelho = ''
for contador in range(1, 5):
    print('-'*5, contador, 'pessoa', '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    totalIdade += idade
    if contador == 1 and sexo in 'Mm':
        idadeHomemVelho = idade
        nomeHomemVelho = nome
    if sexo in 'Mm' and idade > idadeHomemVelho:
        idadeHomemVelho = idade
        nomeHomemVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherMenos20 += 1
média = totalIdade / 4
print('''A média de idade do grupo é de {} anos
O homem mais velho tem {} e se chama {}.
Ao todo são {} mulheres com menos de 20 anos.'''.format(média, idadeHomemVelho, nomeHomemVelho, mulherMenos20 ))
