preçoNormal = float(input('Digite o preço do produto: R$'))
condiçãoDePagamento = int(input('Digite a opção {}1{} para forma de pagamento {}a vista dinheiro/cheque{} ou digite {}2{} para forma de pagamento {}parcelado{}: '.format('\033[1;35m', '\033[m','\033[1;35m', '\033[m','\033[1;34m', '\033[m','\033[1;34m', '\033[m')))
if condiçãoDePagamento == 1:
    valorPago = preçoNormal - preçoNormal*10/100
    print('O valor a ser pago pelo produto será R${}.'.format(valorPago))
if condiçãoDePagamento ==2:
    parcelas = int(input('Em quantas parcelas deseja pagar: '))
    if parcelas == 1 or parcelas == 2:
        valorPago = preçoNormal - preçoNormal*5/100
        print('O valor a ser pago pelo produto será R${}'.format(valorPago))
    else:
        valorPago = preçoNormal + preçoNormal*20/100
        print('O valor a ser pago pelo produto será R${}'.format(valorPago))
