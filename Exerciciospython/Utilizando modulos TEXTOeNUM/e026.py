"""frase = str(input('Digite uma frase: ')).strip()
x = int(len(frase))
print(x)
print('A letra A apareceu em sua frase por {} vezes.'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição {} em sua frase'.format(frase.upper().find('A')))
print('A letra A aparece na posição {} pela última vez na frase.'.format(frase.upper().rfind('A')))"""


frase = str(input('Digite uma frase: ')).upper().strip()
x = int(len(frase))
print(x)
print('A letra A apareceu em sua frase por {} vezes.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {} em sua frase'.format(frase.find('A')+1))
print('A letra A aparece na posição {} pela última vez na frase.'.format(frase.rfind('A')+1))
