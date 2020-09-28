expressão = str(input('Digite sua expresão: '))
print(expressão)
parentesesAbertos = expressão.count("(",0,len(expressão))
parentesFechados = expressão.count(")", 0, len(expressão))
if parentesesAbertos == parentesFechados:
    print('Sua expressão está correta!')
else:
    print('Suan expressão está errada!')

print(len(expressão))
