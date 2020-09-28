v = float(input('Digite o preço do produto: '))
preço =v-( v*5/100)
print('O produto de R${:.2f} com desconto de 5% sai a R${:.2f}'.format(v, preço))