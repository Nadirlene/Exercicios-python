from random import shuffle
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceito nome: ')
a4 = input('Quarto nome: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))
