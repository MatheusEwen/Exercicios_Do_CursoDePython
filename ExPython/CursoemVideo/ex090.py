aluno = {}
aluno['nome'] = str(input('Nome do aluno:'))
aluno['media'] = float(input(f'Media de {aluno["nome"]}:'))
if aluno['media'] < 5:
    aluno['Situação'] = 'Reprovado'
if 5 <= aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
print('='* 30)
for c, v in aluno.items():
    print(f'{c} = {v}')

