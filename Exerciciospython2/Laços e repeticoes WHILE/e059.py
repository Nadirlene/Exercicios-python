from time import sleep
numero01 = float(input('Primeiro valor: '))
numero02 = float(input('Segundo valor: '))
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opcaoEscolhida = int(input('>>>>> Qual é a sua opção? '))
while opcaoEscolhida != 5:
    if  opcaoEscolhida > 5 or opcaoEscolhida <= 0:
       opcaoEscolhida = float(input('Opção inválida, tente outra vez. \n>>>>> Qual é a sua opção? '))
    elif opcaoEscolhida == 1:
        resultado = numero01 + numero02
        print('O resultado de {} + {} é {}'.format(numero01, numero02, resultado))
        print('=-='*10)
        sleep(1)
        opcaoEscolhida = float(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n>>>>> Qual é a sua opção?'))
    elif opcaoEscolhida == 2:
        resultado = numero01 * numero02
        print('O resultado de {} + {} é {}'.format(numero01, numero02, resultado))
        print('=-=' * 10)
        sleep(1)
        opcaoEscolhida = float(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n>>>>> Qual é a sua opção? '))
    elif opcaoEscolhida == 3:
        if numero01 > numero02:
            print('Entre {} e {} o maior valor é {}'.format(numero01, numero02, numero01))
            print('=-=' * 10)
            sleep(1)
            opcaoEscolhida = float(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n>>>>> Qual é a sua opção? '))
        elif numero01 == numero02:
            print('Entre {} e {} o maior valor é {}'.format(numero01, numero02, numero02))
            print('=-=' * 10)
            sleep(1)
            opcaoEscolhida = float(input(
                '[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n>>>>> Qual é a sua opção? '))
        else:
            print('Entre {} e {} o maior valor é {}'.format(numero01, numero02, numero02))
            print('=-=' * 10)
            sleep(1)
            opcaoEscolhida = float(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n>>>>> Qual é a sua opção? '))
    elif opcaoEscolhida == 4:
        print('Informe os números novamente:')
        numero01 = float(input('Primeiro valor: '))
        numero02 = float(input('Segundo valor: '))
        print('=-='*10)
        opcaoEscolhida = float(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n>>>>> Qual é a sua opção? '))
print('Finalizando...')
print('=-=' * 10)
sleep(1)
print('Fim do programa! Volte sempre!')
