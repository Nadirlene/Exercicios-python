from time import sleep
lista = []
def contador(a, b , c):
    if c < 0:
        c *= -1
    elif c == 0:
        c = 1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    sleep(2.5)
    if a <= b:
        cont = a
        while cont <= b:
            print(cont, end=' ')
            cont += c
            sleep(0.5)
        print('FIM !')
    else:
        cont = a
        while cont >= b:
            print(cont, end=' ')
            cont -= c
            sleep(0.5)
        print('FIM !')

contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

