print('{}Comparando dois valores!{}'.format('\033[35m', '\033[m'))
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
if valor1 == valor2:
    print('{}NÃO EXISTE{} valor maior, os dois são {}iguais{}.'.format('\033[1:33m','\033[m', '\033[34m','\033[m'))
elif valor2 > valor1:
    print('O primeiro valor digitado  é menor. \nO segundo valor digitado  é maior')
elif valor1 > valor2:
  print('O primeiro valor digitado é maior. \nO segundo valor digitado é menor.')
