número = int(input('Digite o número que deseja ver sua taboada: '))
for cont in range(0, 11):
    print(' {} x {:2} = {:2}'.format(número, cont , número*cont))
print('FIM')