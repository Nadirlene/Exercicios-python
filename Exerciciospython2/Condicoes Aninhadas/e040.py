nota01 = float(input('Primeira nota: '))
nota02 = float(input('Segunda nota: '))
médiaDasNotas = (nota01 + nota02)/2
if médiaDasNotas < 5:
    print('{}REPROVADO{}'.format('\033[31m', '\033[m'))
elif médiaDasNotas >= 5 and médiaDasNotas <= 6.5:
    print('{}RECUPERAÇÃO{}'.format('\033[33m', '\033[m'))
else:
    print('{}APROVADO!!!{}'.format('\033[34m', '\033[m'))
