resposta = 'S'
soma = contador = maior = menor = 0
while resposta in 'Ss':
    numeroDigitado = int(input('Digite um número: '))
    soma += numeroDigitado
    contador += 1
    if contador == 1:
        maior = menor = numeroDigitado
    resposta = str(input('Você deseja digitar mais números [S/N]: ')).strip().upper()[0]
    if numeroDigitado > maior:
        maior = numeroDigitado
    elif numeroDigitado < menor:
        menor = numeroDigitado
media = soma / contador
print(f'A média dos {contador} números digitados foi {media}. \nO maior valor foi {maior} e o menor foi {menor}')
