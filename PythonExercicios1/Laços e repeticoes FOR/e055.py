maiorPeso = 0
menorPeso = 0
for contador in range(1, 6):
    peso = float(input('Peso {}ª pessoa em Kg:  '.format(contador)))
    if contador == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('''O maior peso apresnetado foi {}Kg 
E menor peso apresentado foi {}Kg.'''.format(maiorPeso,  menorPeso))
