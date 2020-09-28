def notas(* números, sit=False):
    aluno = {}
    aluno['total'] = len(números)
    aluno['maior'] = max(números)
    aluno['menor'] = min(números)
    média = sum(números) / len(números)

    aluno['média'] = média
    if sit:
        if aluno['média'] > 7:
            aluno['situação'] = 'BOA'
        elif 5 <= aluno['média'] < 7:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(2.5, 9.5, 5, 6.5, sit=True)
print(resp)