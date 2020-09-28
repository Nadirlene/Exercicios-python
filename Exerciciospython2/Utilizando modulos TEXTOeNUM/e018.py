import math
a = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O angulo {} tem o SENO de {:.2f} \n COSSENO de {:.2f} \n e TANGENTE de {:.2f}'.format(a, seno, cos, tan))
