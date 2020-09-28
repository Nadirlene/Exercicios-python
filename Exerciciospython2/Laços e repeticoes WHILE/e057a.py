condicao = False
while condicao != True:
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        condicao = True
    elif sexo == 'F':
        condicao = True
    else:
       print('Opção inválida.')
print('Sexo registrado.')