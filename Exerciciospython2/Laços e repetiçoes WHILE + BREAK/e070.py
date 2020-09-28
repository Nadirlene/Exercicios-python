somaProdutos = quantidadeProdutos = 0
maisBarato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    if quantidadeProdutos == 0 or preco < menor:
        menor = preco
        maisBarato = produto
    somaProdutos += preco
    if preco > 1000:
       quantidadeProdutos += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi RS{somaProdutos:.2f}. \n Temos {quantidadeProdutos} custando mais de R$1000.00 ')
print(f'O produto mais barato foi {maisBarato} que custa R${menor}')
