def leiaInt(msg):
    valor = 0

    while True:
        número = str(input(msg))
        if número.isnumeric():
            valor = int(número)
            break
        else:
            print(f'\033[31mERRO! Digite um número válido.\033[m')
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')