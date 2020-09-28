from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de nascimento: '))
idade = date.today().year - anoNascimento
cadastro['idade'] = idade
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
tempo = cadastro['contratação'] + 35
aposentadoria = tempo - anoNascimento
cadastro['aposentar'] = aposentadoria
for k, v in cadastro.items():
    print(f' -{k} tem o valor {v}')

