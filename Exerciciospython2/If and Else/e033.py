número1 = float(input('Primeiro número: '))
número2 = float(input('Segundo número: '))
número3 = float(input('Terceiro número: '))
maior = número1
menor = número1
if número2 > número1 and número2 > número3:
    maior = número2
if número3 > número1 and número3 > número2:
    maior = número3
if número2 < número1 and número2 < número3:
    menor = número2
if número3 < número1 and número3 < número2:
    menor = número3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
