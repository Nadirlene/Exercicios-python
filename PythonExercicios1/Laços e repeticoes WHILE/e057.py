sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
#while sexo != 'M' or sexo != 'F':
while sexo not in 'FM':
    sexo = str(input('Informação inválida. Por favor digite o seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

