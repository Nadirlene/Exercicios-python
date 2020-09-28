salarioAtual = float(input('Digite seu salário atual: R$'))
if salarioAtual > 1250:
    novoSalario = (salarioAtual*10/100) + salarioAtual
    print('Seu novo salário será R${:.2f}'.format(novoSalario))
else:
    novoSalario = (salarioAtual*15/100)+ salarioAtual
    print('Seu novo salário será R${:.2f}'.format(novoSalario))

