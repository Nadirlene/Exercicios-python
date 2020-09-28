while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if valor <= 0:
        break
    for contador in range(0, 11):
        print(f'{valor} x {contador:2} = {valor*contador}')
    print('-'*35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre.')
