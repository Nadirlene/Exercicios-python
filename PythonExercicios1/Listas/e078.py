lista = [int(input('Digite um valor para a Posição 0: ')),
         int(input('Digite um valor para a Posição 1: ')),
         int(input('Digite um valor para a Posição 2: ')),
         int(input('Digite um valor para a Posição 3: ')),
         int(input('Digite um valor para a Posição 4: '))]
print('=-'*20)
print(f'Você digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
for posicao, numero in enumerate(lista):
    if numero == maior:
        print(f'O maior valor digitado foi {numero} na posição {posicao}')
    elif numero == menor:
        print(f'O maior valor digitado foi {numero} na posição {posicao}')
