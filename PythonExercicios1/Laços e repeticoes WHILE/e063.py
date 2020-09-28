print('SEQUENCIA DE FIBONACCI')
print(('-'*23))
n = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
a = 0
b = 1
print(f' {a} -> {b}', end='')
c = a + b
contador = 3
while contador <= n:
    print(f' -> {c}', end=' ')
    a = b
    b = c
    c = a+b
    contador += 1
print('FIM')
print('~'*30)
