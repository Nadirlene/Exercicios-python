ladoA = float(input('Primeiro segmento: '))
ladoB = float(input('Segundo segmento: '))
ladoC = float(input('Terceiro Segmento: '))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print('Os segmentos podem formar um triangulo.')
else:
    print('Os segmentos não podem formar um trinagulo.')