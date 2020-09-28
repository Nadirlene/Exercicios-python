s = 0
n = 0
for contador in range(1, 501, 2):
    if contador % 3 ==0:
        s += contador
        n += 1
print('A soma de todos os {} valores é igual a {:,.2f}'.format(n,s))

