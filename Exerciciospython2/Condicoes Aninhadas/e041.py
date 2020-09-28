from datetime import date
print('{}CONFEDERAÇÃO NACIONAL DE NATAÇÃO{}'.format('\033[1;36m', '\033[m'))
anoNascimento = int(input('Para saber em qual categoria de nadador você pertence \ndigite seu ano de nscimento: '))
idade = date.today().year - anoNascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria {}MIRIM{}'.format('\033[1;36m', '\033[m'))
elif idade <= 14:
    print('Categoria {}INFANTIL{}'.format('\033[1;36m', '\033[m'))
elif idade <= 19:
    print('Categoria {}JUNIOR{}'.format('\033[1;36m', '\033[m'))
elif idade <= 25:
    print('Categoria {}SÊNIOR{}'.format('\033[1;36m', '\033[m'))
else:
    print('Categoria {}MASTER{}'.format('\033[1;36m', '\033[m'))
