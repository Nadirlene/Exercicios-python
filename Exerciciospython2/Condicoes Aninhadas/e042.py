print('Analisando se três segmentos de reta podem ser um triângulo. \nCaso possa, determinar qual tipo de trinagulo.')
segmento01 = float(input('Primeiro segmento: '))
segmento02 = float(input('Segundo segmento: '))
segmento03 = float(input('Terceiro segmento: '))
if segmento01 < segmento02 + segmento03 and segmento02 < segmento01 + segmento03 and segmento03 < segmento01 + segmento02:
    print('Os segmentos podem formar um triangulo!', end='')
    if segmento01 == segmento02 == segmento03:
        print('O triângulo formado será do tipo EQUILÁTERO.')
    elif segmento01 != segmento02 != segmento03 != segmento01:
        print('O triangulo formado será do tipo ESCALENO.')
    else:
        print('O triângulo será do tipo ISÓSCELES.')
else:
    print('Os segmentos NÃO PODEM formar um triânguolo.')