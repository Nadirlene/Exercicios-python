print('CALCULO DE IMC')
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura**2
print('Seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Seu peso é ideal.')
elif 25 <= imc < 30:
    print('Você está na faixa de sobrepeso.')
elif 30 <= imc < 40:
    print('Você está na faixa da obesidade.')
else:
    print('Você está na faixa da obesidade morbida.')
