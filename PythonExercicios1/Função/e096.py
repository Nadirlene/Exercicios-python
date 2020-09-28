def calculoArea(a, b):
    area = a * b
    print(f'A área de um terreno de {a}x{b} é de {area}m².')


print('    Controle de Terrenos')
print('-'*27)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calculoArea(largura, comprimento)
