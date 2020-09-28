distância = float(input('Qual a distância da viagem? '))
if distância>200:
    preçoPassagem = distância * 0.45
    print('Sua passagem vai custar R${:.2f}'.format(preçoPassagem))
else:
    preçoPassagem = distância * 0.50
    print('Sua passagem vai custar R${:.2f}'.format(preçoPassagem))

