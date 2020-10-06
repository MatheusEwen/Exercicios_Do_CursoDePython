def notas(*n, sit = False):
    """
     -->Função para analisar notas e situação de varios alunos
    :param n: uma ou mais notas dos alunos(aceita varias)
    :param sit: valor opcional, indica se deve ou não adicionar a situação
    :return: dicionario com varias informaçoes
    """
    classe = {}
    classe['total'] = len(n)
    classe['maior'] = max(n)
    classe['menor'] = min(n)
    classe['media'] = sum(n)/len(n)

    if sit == True:
        if classe['media'] >= 7:
            classe['situação'] = 'boa'
        elif classe['media'] >= 5:
            classe['situação'] = 'razoavel'
        else:
            classe['situação'] = 'ruim'
    return classe


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)