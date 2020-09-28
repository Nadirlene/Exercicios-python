def leiaInt(msg):
    while True:
        try:
            número = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return número


def leiaFloat(msg):
    while True:
        try:
            número = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        else:
            return número


n = leiaInt('Digite um número inteiro válido: ')
num = leiaFloat('Digite um número real válido: ')
print(f'O valor interio digitado foi {n} e o real foi {num}')