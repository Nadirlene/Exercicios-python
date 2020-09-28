titulo = 'CADASTRE UMA PESSOA'
somaDeMaiores = totalDeHomens = mulheresDeMaior = 0
while True:
    print('-'*30)
    print(f' {titulo}')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
        print('-'*30)
    if idade >= 18:
         somaDeMaiores += 1
    if sexo == 'M':
        totalDeHomens += 1
    if sexo == 'F' and idade < 20:
        mulheresDeMaior +=1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'{somaDeMaiores} pessoas cadastradas com mais de 18 anos. \n{totalDeHomens} homens foram cadastrados.'
      f'\n{mulheresDeMaior} mulheres com menos de 20 anos')