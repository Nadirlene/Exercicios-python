n�mero = int(input('Digite um n�mero inteiro: '))
print('''Escolha uma das bases para convers�o:
[ 1 ] converter para BIN�RIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op��oDeConvers�o = int(input('Sua op��o: '))
if op��oDeConvers�o == 1:
    print('{} convertido para BIN�RIO � igual a {}.'.format(n�mero, bin(n�mero)[2:]))
elif op��oDeConvers�o == 2:
    print('{} convertido para OCTAL � igual a {}.'.format(n�mero, oct(n�mero)[2:]))
elif op��oDeConvers�o == 3:
    print('{} convertido para OCTAL � igual a {}.'.format(n�mero, hex(n�mero)[2:]))
else:
    print('Op��o inv�lida. Tente novamente.')
