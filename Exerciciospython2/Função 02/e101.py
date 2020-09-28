def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if 16 <= idade < 18 or idade >= 65:
        return f'VOTO FACULTAVIO.'
    elif 18 <= idade < 65:
        return f'VOTO OBRIGATÓRIO.'
    else:
        return 'NÃO VOTA'


anoNascimento = int(input('Em que ano você nasceu? '))
print(voto(anoNascimento))

