from time import sleep
def maior(* números):
    print('-='*30)
    print('Analisando os valores passados...')
    contador = maior = 0
    for valor in números:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1

    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()