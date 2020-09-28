resultado = dict()
resultado['nome'] = str(input('Nome: '))
resultado['média'] = float(input(f'Média de {resultado["nome"]}: '))
if resultado['média'] < 5:
    resultado['situação'] = 'REPROVADO'
elif 5 <= resultado['média'] < 7:
    resultado['situação'] = 'EM RECUPERAÇÃO'
elif resultado['média'] >= 7:
    resultado['situação'] = 'APROVADO'
print(resultado)
print('-='*30)
for k, v in resultado.items():
    print(f'    - {k} é igual a {v}')

