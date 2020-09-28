'''co = float(input('Qual é o comprimento do cateto oposto: '))
ca = float(input('Qual é o comprimento do cateto adjacente: '))
from math import sqrt
print('A hipotenusa vai medir {:.2f} '.format(sqrt(co**2 + ca**2)))'''


import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vale {:.2f}'.format(hi))
