from datetime import date
print('{}Vamos ver sua situação quanto ao alistamento militar!!{}'.format('\033[1:31m', '\033[m'))
anoNascimento = int(input('Digite o seu ano de nascimento: '))
idadeAtual = date.today().year - anoNascimento
if idadeAtual < 18:
    tempoParaAlistamento = 18 - idadeAtual
    print('Você {}ainda vai se alistar ao serviço militar{} e isso será daqui a {}{}{} anos.'.format('\033[36m', '\033[m', '\033[36m', tempoParaAlistamento, '\033[m', ))
elif idadeAtual == 18:
    print('{}Já é hora{} de se alistar!!!'.format('\033[33m', '\033[m'))
else:
    tempoParaAlistamento = idadeAtual - 18
    print('O seu {}período para alistamento ja encerrou{} a {}{}{} anos.'.format('\033[34m', '\033[m', '\033[34m', tempoParaAlistamento, '\033[m'))




