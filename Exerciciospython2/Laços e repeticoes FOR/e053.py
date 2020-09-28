frase = str(input('Digite uma frase: ')).strip()
fraseJunta = frase.upper().split()
fraseSemEspaço = ''.join(fraseJunta)
#inversoFrase = ''
'''for posiçãoLetra in range(len(fraseSemEspaço)-1, -1, -1):
    inversoFrase += fraseSemEspaço[posiçãoLetra]'''
inversoFrase = fraseSemEspaço[::-1]
if inversoFrase == fraseSemEspaço:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo')
print(fraseSemEspaço, inversoFrase)


