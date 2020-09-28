valorCasa = float(input('Digite o valor da casa que deseja comprar: R$'))
salarioComprador = float(input('Digite seu atual salário: R$'))
anosFinaciamento = float(input('Digite em quantos anos deseja pagar: '))
valorPrestacões = valorCasa / (anosFinaciamento*12)
print(valorPrestacões)
limitePrestação = salarioComprador * 30/100
print(limitePrestação)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorCasa, anosFinaciamento), end='')
print('a prestação será de R${:.2f}'.format(valorPrestacões))
if valorPrestacões >= limitePrestação:
    print('{}Empréstimo negado! Infelizmnete você não poderá financiar essa casa.{}'.format('\033[1;31m', '\033[m'))
else:
    print('{}PARABÉNS! Seu emprestimo foi aprovado com sucesso.{}. \nSua casa será paga em {} de R${:.2f}'.format('\033[32m', '\033[m', anosFinaciamento*12, valorPrestacões))